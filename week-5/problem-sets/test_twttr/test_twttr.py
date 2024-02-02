from twttr import shorten

def test_uppercase():
    assert shorten("HARVARD") == "HRVRD"
    assert shorten("YALE") == "YL"

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("lianli") == "lnl"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("March 23") == "Mrch 23"

def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("how's it going?") == "hw's t gng?"
