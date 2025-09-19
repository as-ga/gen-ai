from openai import OpenAI
from dotenv import load_dotenv
import os

import requests

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_API_URL"),
)


def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The current weather in {city.capitalize()} is: {response.text}"

    return "Sorry, I couldn't fetch the weather information right now."


def main():
    user_query = input("🤔: ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": user_query}],
    )
    print("🤖:", response.choices[0].message.content)


# main()
print(get_weather("lucknow"))

#  what is the current weather in Lucknow and date?
