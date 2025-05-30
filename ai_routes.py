from flask import Blueprint, request, Response, stream_with_context
from openai import OpenAI
import os
import sqlite3

ai_bp = Blueprint("ai", __name__)
client = OpenAI(api_key="api-key")


# SQLite cache
def init_db():
    with sqlite3.connect("cache.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS prompts (prompt TEXT PRIMARY KEY, response TEXT)")

init_db()

def get_cached_response(prompt):
    with sqlite3.connect("cache.db") as conn:
        cur = conn.execute("SELECT response FROM prompts WHERE prompt = ?", (prompt,))
        row = cur.fetchone()
        return row[0] if row else None

def cache_response(prompt, response):
    with sqlite3.connect("cache.db") as conn:
        conn.execute("INSERT OR REPLACE INTO prompts (prompt, response) VALUES (?, ?)", (prompt, response))

@ai_bp.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return {"error": "No prompt provided"}, 400

    cached = get_cached_response(prompt)
    if cached:
        return Response(cached, content_type="text/plain")

    def generate():
        response_text = ""
        try:
            stream = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system", "content": "You are an expert in Dr. Leif's Papers on Fusion, Physics, and Engineering"},
                    {"role": "user", "content": prompt}
                ],
                stream=True,
                max_tokens=4000,
                temperature=0.7,
                top_p=1
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                response_text += delta
                yield delta
            cache_response(prompt, response_text)
        except Exception as e:
            yield f"[Error] {str(e)}"

    return Response(stream_with_context(generate()), content_type="text/plain")
