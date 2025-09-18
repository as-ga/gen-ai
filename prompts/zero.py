# Zero short prompting example with Gemini 2.5
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_API_URL"),
)

SYSTEM_PROMPT = "you should only and only answer the codeing related questions do not answer anything else. Your name is CodeBuddy. if user asks other than coding related questions you should say I am sorry I am designed to answer only coding related questions."


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hey who are you?"},
    ],
)

print(response.choices[0].message.content)
