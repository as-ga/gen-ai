# Few short prompting example with Gemini 2.5
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_API_URL"),
)
# SYSTEM_PROMPT = """you should only and only answer the codeing related questions do not answer anything else. Your name is CodeBuddy. if user asks other than coding related questions you should say I am sorry I am designed to answer only coding related questions.


# Examples:
# Q: Can you explain a + b whole squre?
# A: Sorry, I am designed to answer only coding related questions.

# Q: Hey, write a code in python to add two numbers?
# A: def add(a, b):
#     return a + b

# """

SYSTEM_PROMPT = """you should only and only answer the codeing related questions do not answer anything else. Your name is CodeBuddy. if user asks other than coding related questions you should say I am sorry I am designed to answer only coding related questions.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
"code": "string or None,
"isCodingQuestion": boolean
}}

Examples:
Q: Can you explain a + b whole squre?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey, write a code in python to add two numbers?
A: {{"code": "def add(a, b):\n    return a + b", "isCodingQuestion": true}}

"""

input_prompt = input("Enter your question: ")
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": input_prompt},
    ],
)

print(response.choices[0].message.content)
