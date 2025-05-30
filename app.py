from flask import Flask, render_template, jsonify, request
import json
from ai_routes import ai_bp  # Import your AI Blueprint!

app = Flask(__name__)
app.register_blueprint(ai_bp)  # Register it here!

# Tech data
TECH = [
    {
        "id": 1,
        "title": "Quantum Circuits",
        "summary": "Gate-based quantum computing.",
        "keywords": ["qubits", "Hadamard", "entanglement"],
        "details": "Quantum circuits use unitary gates to perform logical operations on qubits."
    },
    {
        "id": 2,
        "title": "Quantum AI",
        "summary": "AI models for quantum control.",
        "keywords": ["machine learning", "QML"],
        "details": "Quantum AI leverages machine learning to optimize quantum systems."
    },
    {
        "id": 3,
        "title": "Cryogenics",
        "summary": "Supercooled environments for qubits.",
        "keywords": ["dilution refrigerator", "temperature"],
        "details": "Cryogenics is essential to achieve superconductivity at millikelvin temperatures."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/technologies")
def technologies():
    return jsonify([{k: v for k, v in t.items() if k != "details"} for t in TECH])

@app.route("/api/technology/<int:tech_id>")
def technology_detail(tech_id):
    for t in TECH:
        if t["id"] == tech_id:
            return jsonify(t)
    return jsonify({"error": "not found"}), 404

@app.route("/api/search")
def search():
    query = request.args.get("q", "").lower()
    if not query:
        return {"results": []}
    with open("data/processed_superconductors.json") as f:
        materials = json.load(f)
    results = [
        m for m in materials
        if query in m["name"].lower() or query in m["formula"].lower()
    ]
    return {"results": results}

if __name__ == "__main__":
    app.run(debug=True)
