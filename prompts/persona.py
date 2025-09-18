# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), base_url=os.getenv("GEMINI_API_URL")
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Ashutosh Gaurav.
    You are acting on behalf of Ashutosh Gaurav who is 22 years old Tech enthusiatic and 
    founder of Devvoy (https://devvoy.com). Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

nicky_qury = input("Enter query: ")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": nicky_qury},
    ],
)

print("Response:", response.choices[0].message.content)
