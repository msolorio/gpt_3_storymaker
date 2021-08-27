import os
import openai
import keyboard
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

total_text = input('Please provide an opening line: ')

while True:
  response = openai.Completion.create(
    engine="davinci",
    prompt=total_text,
    temperature=0.9,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  text_response = response.choices[0].text
  total_text += text_response

  print(text_response, end='')

  keyboard.wait('space')
