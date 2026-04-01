transactions = []
def add_transaction(name, amount):
    transactions.append({"name": name, "amount": amount})
def list_transactions():
    return transactions
def get_balance():
    return sum(t["amount"] for t in transactions)
