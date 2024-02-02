from plates import is_valid

def test_isvalid():
    assert is_valid("BEN12") == True
    assert is_valid("0B") == False

def test_twoletter(): #“All vanity plates must start with at least two letters.”
    assert is_valid("CDE12") == True
    assert is_valid("C1345") == False

def test_length(): #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    assert is_valid("AAA222") == True
    assert is_valid("AAAA2222") == False

def test_number(): #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    assert is_valid("ABCD12") == True
    assert is_valid("AA22CD") == False
    assert is_valid("0A22CD") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("00") == False
    assert is_valid("CS05") == False

def test_character(): #“No periods, spaces, or punctuation marks are allowed.”
    assert is_valid("CS50!!") == False
    assert is_valid("P3.14") == False
