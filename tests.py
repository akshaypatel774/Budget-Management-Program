from project import validate_currency, validate_input, validate_amount

def test_validate_currency():
    assert validate_currency("1") == "$"
    assert validate_currency("2") == "£"
    assert validate_currency("3") == "€"
    assert validate_currency("4") == "₹"
    assert validate_currency("USD") == None

def test_validate_input():
    assert validate_input("1") == "1"
    assert validate_input("2") == "2"
    assert validate_input("q") == "q"
    assert validate_input("a") == None
    assert validate_input("") == None

def test_validate_amount():
    assert validate_amount("100") == 100.0
    assert validate_amount("500") == 500.0
    assert validate_amount("0") == 0.0
    assert validate_amount("@$") == None
    assert validate_amount("amount") == None
    assert validate_amount("") == None