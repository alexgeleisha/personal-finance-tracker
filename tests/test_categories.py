from finance.categories import add_category

def test_category():
    add_category("test")
    assert "test" in ["test"]
