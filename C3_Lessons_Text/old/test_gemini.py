import os
import google.genai as genai
try:
    client = genai.Client()
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Hello'
    )
    print("Success:", response.text)
except Exception as e:
    print("Error:", e)
