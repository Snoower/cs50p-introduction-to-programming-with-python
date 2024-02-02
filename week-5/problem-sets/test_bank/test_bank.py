from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HeLlO") == 0

def test_h():
    assert value("hi") == 20
    assert value("heeeeeeee") == 20
    assert value("HI") == 20

def test_other():
    assert value("bee") == 100
    assert value("BEE") == 100
    assert value("0") == 100
    assert value("100") == 100
