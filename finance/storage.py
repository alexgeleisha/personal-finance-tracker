import json
def save(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)
def load(filename="data.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except:
        return []
save(transactions)
