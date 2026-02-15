import sys
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient

class VisionClient:
    """
    Handles Image-to-Text extraction using GeminiClient.
    Ensures strict diacritic preservation for Arabic grammar content.
    """
    
    def __init__(self, api_key=None, project_root=None):
        self.client = GeminiClient(api_key, project_root)
        
    def extract_text(self, image_paths):
        """
        Sends images to Gemini and requests a raw transcription.
        """
        if not image_paths:
            print("⚠️ No images provided for extraction.")
            return ""

        print(f"👁️ VisionClient: Processing {len(image_paths)} images...")

        # Strict Prompt
        system_instruction = (
            "You are an expert Arabic OCR engine. "
            "Transcribe the Arabic text from these educational images EXACTLY as it appears. "
            "Preserve all diacritics (Harakat) strictly. "
            "Do not summarize. Do not explain. Just output the raw Arabic text. "
            "If there are headers, use markdown headers (#). "
            "If there are tables, represent them as markdown tables. "
            "Ignore page numbers or irrelevant footer text."
        )

        # Call generic client
        # Pass images as list of paths
        return self.client.generate_content(
            system_instruction=system_instruction,
            user_content="", # No extra user text needed beyond the system instruction/images
            images=image_paths
        )

if __name__ == "__main__":
    client = VisionClient()
    print("VisionClient (Refactored) initialized.")