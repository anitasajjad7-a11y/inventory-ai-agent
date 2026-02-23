from flask import Flask, render_template, request, jsonify
from agents.inventory_agent import InventoryAgent

app = Flask(__name__)
agent = InventoryAgent()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    answer = agent.answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)