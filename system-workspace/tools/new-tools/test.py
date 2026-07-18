import openai

client = openai.OpenAI(api_key="sk-antigravity", base_url="http://127.0.0.1:8045/v1")

response = client.chat.completions.create(
    model="gemini-3-flash",
    messages=[{"role": "user", "content": "Hello, please introduce yourself"}],
)
print(response.choices[0].message.content)
