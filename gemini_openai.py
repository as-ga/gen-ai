from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(api_key=os.getenv("LLM_API_KEY"), base_url=os.getenv("LLM_API_URL"))

response = client.chat.completions.create(
    model="gemini-2.5-flash", messages=[{"role": "user", "content": "who are you"}]
)

print(response.choices[0].message.content)
