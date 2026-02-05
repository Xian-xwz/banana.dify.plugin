# Banana 图像生成插件

基于 Google Gemini API 的图像生成插件，支持 Banana/Nano Banana 图像生成服务。

## 功能

- 支持 Gemini 2.0/2.5 Flash 图像生成模型
- 可自定义图像尺寸（宽度和高度）
- 支持 2K/4K 质量选项
- 直接在 Dify 工作流中生成图像

## 安装

1. 在 Dify 插件市场中选择"通过 GitHub 安装"
2. 输入仓库地址：`https://github.com/Xian-xwz/banana.dify.plugin`
3. 安装完成后，在插件设置中配置您的 Gemini API Key

## 配置

在 Dify 中配置 Banana 插件时，需要提供：
- **API Key**: 您的 Google Gemini API Key
  - 获取地址：https://aistudio.google.com/app/apikey

## 使用方法

安装并配置后，可以在 Dify 的工作流中添加 "Generate Image" 工具节点：

1. **Prompt**: 输入图像描述（支持中英文）
2. **Width/Height**: 设置图像尺寸（默认 1024x1024）
3. **Model**: 选择使用的模型
   - Gemini 2.0 Flash Image Generation（实验版）
   - Gemini 2.5 Flash Image
4. **Quality**: 选择图像质量（2K 或 4K）

## 模型说明

| 模型 | 特点 | 适用场景 |
|------|------|----------|
| Gemini 2.0 Flash Image | 快速、成本低 | 日常图像生成 |
| Gemini 2.5 Flash Image | 更高质量 | 专业图像生成 |

## 注意事项

- 图像生成需要消耗 API 配额
- 请妥善保管您的 API Key
- 生成的图像受 Gemini API 使用政策约束

## 作者

- **GitHub**: [Xian-xwz](https://github.com/Xian-xwz)

## 许可证

MIT License
