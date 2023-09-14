# Global Code
import openai
import os
import preprocessing
import re

def request(apikey, prompt, mcdata, engine, temperature, onlocal):

  if not onlocal:
    if not os.getenv("OPENAI_API_KEY"):
      apikey = apikey
    else:
      apikey = os.getenv("OPENAI_API_KEY")
    openai.api_key = apikey

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": ""
        }
      ],
      temperature=0.05,
      max_tokens=40,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    # GPT-3の応答を取得
    generated_text = response.choices[0].text

    # 応答を表示
    print(generated_text)