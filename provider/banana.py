from dify_plugin import ToolProvider


class BananaProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict) -> None:
        """
        验证凭证是否有效
        """
        if not credentials.get("gemini_api_key"):
            raise ValueError("Gemini API Key is required")
