#FLASK_APP=app
#FLASK_ENV=development

# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
#OPENAI_API_KEY= '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'

#cd openai-quickstart-python
#cp .env.example .env

import os
import openai
openai.api_key = "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"
'''
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
'''