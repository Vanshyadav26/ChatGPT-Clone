from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import openai, os, datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
messages = db.messages

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

def history(session_id):
    docs = messages.find({"session_id": session_id}).sort("created_at", 1)
    return [{"role": d["role"], "content": d["content"]} for d in docs]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json or {}
    sid = data.get("session_id")
    prompt = data.get("message", "")
    chain = history(sid) + [{"role": "user", "content": prompt}]
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chain)
    reply = res.choices[0].message["content"]
    ts = datetime.datetime.utcnow()
    messages.insert_many([
        {"session_id": sid, "role": "user", "content": prompt, "created_at": ts},
        {"session_id": sid, "role": "assistant", "content": reply, "created_at": ts},
    ])
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
