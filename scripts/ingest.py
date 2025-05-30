import json

# Normally you'd download or read a CSV file here.
# For now, we'll use a static list as a mock dataset.

data = [
    {"name": "YBa2Cu3O7", "formula": "YBa2Cu3O7", "Tc_K": 92, "discovery": "1987"},
    {"name": "HgBa2Ca2Cu3O8", "formula": "HgBa2Ca2Cu3O8", "Tc_K": 133, "discovery": "1993"},
    {"name": "LaFeAsO", "formula": "LaFeAsO", "Tc_K": 26, "discovery": "2008"},
    {"name": "Bi2Sr2Ca2Cu3O10", "formula": "Bi2Sr2Ca2Cu3O10", "Tc_K": 110, "discovery": "1995"},
]

with open("processed_superconductors.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Superconductor data saved to processed_superconductors.json")
