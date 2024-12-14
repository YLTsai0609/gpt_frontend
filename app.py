import os

import openai
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

# 載入 .env 檔案中的環境變數
load_dotenv()

app = Flask(__name__)

# 設定 OpenAI API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")
os.getenv("API_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=[{"role": "user", "content": user_input}]
    )
    # 假設回應中包含文字和可能的圖片 URL
    chat_response = response.choices[0].message["content"]
    return jsonify({"response": chat_response})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
