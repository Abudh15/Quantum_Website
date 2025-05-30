# API Reference

This project supports the following endpoints:

---

### `GET /api/technologies`

Returns a list of featured quantum technologies.

**Response**
```json
[
  {
    "title": "Quantum Circuits",
    "summary": "Gate-based quantum computing.",
    "keywords": ["qubits", "Hadamard", "entanglement"]
  },
  ...
]
```

---

### `GET /api/search?q=QUERY`

Search for superconductors by name or formula.

**Response**
```json
{
  "results": [
    {
      "name": "LaFeAsO",
      "formula": "LaFeAsO",
      "Tc_K": 26,
      "discovery": "2008"
    }
  ]
}
```

---

### `POST /api/ask`

Ask the AI chat agent a question.

**Request Body**
```json
{
  "prompt": "What is quantum tunneling?"
}
```

**Streaming Response**
Plain text streamed token-by-token from OpenAI.
