import pytest
from project import translate, identify, get_language_code

def test_translate():
    assert translate('potato', 'en', 'ko') == "감자"
    assert translate('potato', 'en', 'tl') == "patatas"
    assert translate('potato', 'en', 'ja') == "じゃがいも"

def test_identify():
    assert identify("감자") == "Language: korean"
    assert identify("じゃがいも") == "Language: japanese"
    assert identify("potato") == "Language: english"

def test_get_language_code():
    assert get_language_code("korean") == "ko"
    assert get_language_code("japanese") == "ja"
    assert get_language_code("filipino") == "tl"

def test_value_error():
    with pytest.raises(ValueError):
        assert translate('potato', 'en', 'dadafewqr') #invalid language
