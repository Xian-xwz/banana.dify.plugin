# -*- coding: utf-8 -*-
"""
Banana 图像生成工具
"""
import base64
import requests
from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class GenerateImageTool(Tool):
    """图像生成工具"""

    def _invoke(
        self,
        tool_parameters: dict[str, Any],
        user_id: str,
        conversation_id: str | None = None,
        app_id: str | None = None,
        message_id: str | None = None,
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        调用图像生成工具
        """
        # 获取参数
        prompt = tool_parameters.get("prompt", "")
        width = int(tool_parameters.get("width", 1024))
        height = int(tool_parameters.get("height", 1024))
        model = tool_parameters.get("model", "gemini-2.0-flash-exp-image-generation")
        quality = tool_parameters.get("quality", "2k")

        # 从凭证中获取 API Key
        api_key = self.runtime.credentials.get("api_key", "")

        if not api_key:
            yield self.create_text_message("错误: 未配置 API Key")
            return

        try:
            # 调用 API 生成图像
            image_data = self._call_api(prompt, width, height, model, api_key, quality)

            # 返回图像
            yield self.create_blob_message(
                blob=image_data,
                meta={
                    "mime_type": "image/png",
                    "width": width,
                    "height": height,
                },
            )

        except Exception as e:
            yield self.create_text_message(f"图像生成失败: {str(e)}")

    def _call_api(
        self,
        prompt: str,
        width: int,
        height: int,
        model: str,
        api_key: str,
        quality: str = "2k",
    ) -> bytes:
        """
        调用 Gemini API 生成图像

        Args:
            prompt: 图像提示词
            width: 图像宽度
            height: 图像高度
            model: 使用的模型
            api_key: API 密钥
            quality: 图像质量

        Returns:
            图像数据（bytes）
        """
        # 构建请求体
        request_body = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"Generate an image: {prompt}. Image size: {width}x{height}, quality: {quality}"
                        }
                    ]
                }
            ],
            "generationConfig": {
                "responseModalities": ["Text", "Image"],
            },
        }

        # API 端点
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

        # 请求头
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        }

        # 发送请求
        response = requests.post(url, headers=headers, json=request_body)

        if response.status_code != 200:
            raise Exception(f"API 请求失败: {response.status_code} - {response.text}")

        # 解析响应
        result = response.json()

        # 提取图像数据
        if "candidates" in result and len(result["candidates"]) > 0:
            candidate = result["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                for part in candidate["content"]["parts"]:
                    if "inlineData" in part:
                        # 提取 base64 图像数据
                        image_data = base64.b64decode(part["inlineData"]["data"])
                        return image_data

        raise Exception("未能从 API 响应中提取图像数据")
