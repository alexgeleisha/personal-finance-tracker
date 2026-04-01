from finance.tracker import add_transaction, get_balance

def test_balance():
    add_transaction("Test", 10)
    assert get_balance() >= 10
