from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/infer", methods=["POST"])
def infer():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing query"}), 400
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are the Ritual Oracle."},
            {"role": "user", "content": query}
        ]
    )
    return jsonify({"result": completion.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
