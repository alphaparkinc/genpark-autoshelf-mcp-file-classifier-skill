class AutoShelfMcpFileClassifierClient:
    def classify_file(self, file_name: str, file_content_preview: str) -> dict:
        folder = "financials" if "invoice" in file_name.lower() or "price" in file_content_preview.lower() else "general"
        return {"suggested_directory": f"/documents/{folder}"}