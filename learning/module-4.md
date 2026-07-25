# Module 4: AI, OCR & Automation Pipelines

Welcome to Module 4. We have now reached the "Brain" of the repository. 

How does the system actually extract complex Arabic grammar rules, complete with strict diacritics (Tashkeel), from flat image files? How does it communicate with the AI without hallucinating incorrect grammar?

In this module, we dive into the `system-workspace/tools/automation/modules/` directory. We will look at exactly how the custom `GeminiClient` wraps the Google Gemini API, how the `VisionClient` handles images, and the strict Prompt Engineering used to keep the AI on track.

---

## Beginner Primer: Navigating JSON Dictionaries

When the AI finishes processing an image, it doesn't just hand us a plain string. It hands us a massive, nested data structure called JSON (JavaScript Object Notation). It looks like a Russian Nesting Doll of Python dictionaries and lists.

Beginners often get terrified when they see code like this:
`text = response_json['candidates'][0]['content']['parts'][0]['text']`

**How to read this step-by-step:**
1. **`['candidates']`**: Open the first box. It contains a list of possible AI answers.
2. **`[0]`**: Grab the very first answer from that list (Index 0).
3. **`['content']`**: Open the content box of that answer.
4. **`['parts']`**: Open the parts list.
5. **`[0]`**: Grab the first part.
6. **`['text']`**: Finally, pull out the actual raw Arabic text string!

---

## Lesson 1: AI Orchestration & API Communication

Instead of relying heavily on massive SDKs, this repository uses a lightweight, direct REST API client for Google Gemini. This prevents dependency bloat and allows the system to easily fallback to headless CLI commands if standard network requests fail.

Let's look at the `GeminiClient` class located in `gemini_client.py`.

### Real Code: Formatting Images for the API

When sending an image to Gemini, it must be encoded into a specific Base64 string format. Here is the exact code the repository uses:

```python
# From gemini_client.py
        # Process Images
        if images:
            for img_path in images:
                img_path = Path(img_path)
                if not img_path.exists():
                    print(f"⚠️ Image not found: {img_path}")
                    continue

                try:
                    with open(img_path, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

                    mime_type = "image/jpeg"
                    if img_path.suffix.lower() == ".png":
                        mime_type = "image/png"
                    elif img_path.suffix.lower() == ".webp":
                        mime_type = "image/webp"

                    parts.append({"inline_data": {"mime_type": mime_type, "data": encoded_string}})
                except Exception as e:
                    print(f"❌ Error reading image {img_path}: {e}")

        payload = {"contents": [{"parts": parts}], "generationConfig": {"temperature": 0.0}}
```

**Line-by-Line Breakdown:**
1.  **`with open(img_path, "rb")`**: Notice the `"rb"` (Read Binary). Images cannot be read as standard `utf-8` text. They must be read as raw binary data.
2.  **`base64.b64encode(...)`**: The Google API only accepts text strings via REST. We convert the raw binary image data into a massive string of characters (Base64).
3.  **`mime_type`**: The API needs to know if the Base64 string is a JPEG, PNG, or WEBP.
4.  **`{"temperature": 0.0}`**: **CRITICAL RULE.** AI temperature controls creativity. A temperature of 1.0 means the AI is highly creative (and likely to hallucinate). In an Arabic Grammar book, creativity is disastrous. We set the temperature to `0.0` to force absolute, deterministic, robotic precision.

---

## Lesson 2: Prompt Engineering for Arabic Grammar

If you send an image of a book to an AI and say "Transcribe this", the AI will often reply with: *"Sure! Here is the transcription of the image you provided: [Text]"*

That conversational filler completely breaks our automated pipeline! If Python tries to inject *"Sure! Here is..."* into our HTML template, the page is ruined. 

To prevent this, we use the `VisionClient` (found in `vision.py`). It applies a highly restrictive "System Instruction".

### Real Code: The OCR Prompt

```python
# From vision.py
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
        return self.client.generate_content(
            system_instruction=system_instruction,
            user_content="Transcribe this image.",  # Explicit user prompt to anchor the request
            images=image_paths,
        )
```

**Line-by-Line Breakdown:**
*   **`"You are an expert Arabic OCR engine."`**: Setting the Persona. We tell the LLM it is not a chatbot; it is a mechanical OCR engine.
*   **`"1. Preserve all diacritics..."`**: The most important rule. Arabic grammar (I'rab) depends entirely on the ending vowels (Fatha, Damma, Kasra). If the AI strips them, the book is useless.
*   **`"2. Output ONLY the raw Arabic text..."` & Rule 6**: These rules explicitly ban the "Sure! Here is..." hallucination, ensuring our pipeline only receives parsable data.
*   **`"user_content="Transcribe this image."`**: The system instruction acts as the background rules, while this acts as the direct trigger command.

---

## Lesson 3: Workflow Execution

Once `VisionClient` extracts the perfect, diacritized Arabic text, what happens?

It hands the raw markdown text over to the **Planner Module** (`jules_planner.py`). 
The Planner takes the raw text and makes *another* API call to Gemini. But this time, it provides the `Jules-workspace/design_patterns.json` we learned about in Module 0. 

It tells the AI: *"Take this raw text, look at these JSON design rules, and break the text down into structured Dataclasses."*

Once the AI returns structured JSON, Python loops over it and injects it into HTML (exactly as we practiced in Module 1). 

---

## Lesson 4: Practical Exercise (REST API Sandbox)

To truly understand the AI engine, here is a mini-script you can run locally. It bypasses our internal wrapper and shows you exactly how Python talks to a REST API. 

*(Note: You will need a valid Gemini API key to run this successfully).*

```python
import json
import requests

# 1. Setup your key (Replace with your actual key)
API_KEY = "YOUR_GEMINI_API_KEY"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

# 2. Define the Strict OCR Prompt
system_instruction = "You are an OCR engine. Output ONLY raw Arabic text with full diacritics. No chat."
user_prompt = "Transcribe the image. (For this sandbox, just translate 'The Subject is Nominative' to Arabic with Tashkeel)."

# 3. Build the Payload exactly as gemini_client.py does
payload = {
    "systemInstruction": {
        "parts": [{"text": system_instruction}]
    },
    "contents": [
        {"parts": [{"text": user_prompt}]}
    ],
    "generationConfig": {
        "temperature": 0.0  # Zero creativity, high precision
    }
}

# 4. Make the HTTP Request
headers = {'Content-Type': 'application/json'}
response = requests.post(URL, headers=headers, data=json.dumps(payload))

# 5. Parse the Response
if response.status_code == 200:
    data = response.json()
    # The API returns a deeply nested dictionary. We must extract the specific text.
    extracted_text = data['candidates'][0]['content']['parts'][0]['text']
    print("✅ AI Response:")
    print(extracted_text)
else:
    print(f"❌ Error {response.status_code}: {response.text}")
```

### Review
You now understand how the AI Orchestrator operates. 
*   You know how images are converted to Base64 strings.
*   You understand why `temperature: 0.0` is strictly enforced.
*   You know the exact Prompt Engineering commands used to prevent conversational filler and preserve Tashkeel.

In **Module 5: The HTML Engine & The 1-Page Law**, we will look at what happens *after* the AI returns the structured data, and how the system calculates if the generated HTML will actually fit onto a single A4 piece of paper!
