"""
https://platform.openai.com/docs/quickstart?language-preference=python
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# 載入 .env 檔案中的環境變數
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "尼好，請說繁體中文，再加一點新時代網路梗"},
    ],
)

print(completion.choices[0].message.content)
