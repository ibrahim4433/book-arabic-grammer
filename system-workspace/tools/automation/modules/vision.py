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
            "Your task is to transcribe the Arabic text from the provided image EXACTLY as it appears. "
            "1. Preserve all diacritics (Harakat) strictly. "
            "2. Output ONLY the raw Arabic text. Do not add any introduction, explanation, or conversational filler. "
            "3. If there are headers, use markdown headers (#). "
            "4. If there are tables, represent them as markdown tables. "
            "5. Ignore page numbers or irrelevant footer text. "
            "6. Do NOT say 'Here is the transcription' or similar. Just the Arabic text."
        )

        # Call generic client
        # Pass images as list of paths
        return self.client.generate_content(
            system_instruction=system_instruction,
            user_content="Transcribe this image.",  # Explicit user prompt to anchor the request
            images=image_paths,
        )


if __name__ == "__main__":
    client = VisionClient()
    print("VisionClient (Refactored) initialized.")
