categories = ["food", "salary"]
def add_category(name):
    categories.append(name)
def add_transaction(name, amount, category=None):
    transactions.append({
        "name": name,
        "amount": amount,
        "category": category
    })
def list_categories():
    return categories
category = category or "other"
