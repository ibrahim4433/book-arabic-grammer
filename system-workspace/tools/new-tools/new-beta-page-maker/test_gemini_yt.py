import os

import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content(
    ["Please transcribe this video:", "https://www.youtube.com/watch?v=CCs4ID1pu-I"]
)
print(response.text)
