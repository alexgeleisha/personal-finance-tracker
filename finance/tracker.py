transactions = []
def add_transaction(name, amount):
    transactions.append({"name": name, "amount": amount})
def list_transactions():
    return transactions
