import os
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = './key.env'
load_dotenv(dotenv_path=dotenv_path)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generateSchedule(phrase):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": "I will give you some words or phrases from the subject. Some words are abbreviations or abbreviations. I hope you will standardize this word or phrase. You don't need to reply with sentences, you just need to reply with the words or phrases you converted and nothing else. Here is the word: " + phrase + "."}
    ]
  )

  return completion.choices[0].message.content

#print(generateSchedule("cs").content)
#docker exec -it -d server-db-3 python3 -m jupyterlab --no-browser --ip=0.0.0.0 --port=5000 --allow-root --NotebookApp.token=''
