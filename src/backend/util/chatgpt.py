import os
import openai

openai.api_key = ""

def generateSchedule(sentence):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": sentence}
    ]
  )

  return completion.choices[0].message["content"]
