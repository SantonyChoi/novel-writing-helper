import os
import openai
import dotenv
from flask import Flask, render_template, request, jsonify

# Set your OpenAI API key from an environment variable
# OPENAI_API_KEY
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder="../client")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/api/generate-conversation", methods=["POST"])
def generate_conversation():
    data = request.get_json()
    prompt = data["prompt"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7,
        )
        print(response)
        generated_text = response.choices[0].message.content
        return jsonify({"result": generated_text})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error generating conversation. Please try again."})


if __name__ == "__main__":
    app.run(debug=True)
