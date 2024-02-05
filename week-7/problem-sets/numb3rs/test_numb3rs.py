from numb3rs import validate

def test_ip():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.47") == True
    assert validate("300.300.300.300") == False
    assert validate("75.456.76.650") == False
    assert validate("199.999.299.800") == False
    assert validate("potato") == False
    assert validate("555.555.555.555") == False

