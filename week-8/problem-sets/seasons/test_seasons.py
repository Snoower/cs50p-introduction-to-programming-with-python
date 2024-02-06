from seasons import Date
import pytest

class TestMyClass:
    def test_invalid_output(cls):
        with pytest.raises(SystemExit, match="Invalid date"):
            Date.convert("January 1, 1999")
        with pytest.raises(SystemExit, match="Invalid date"):
            Date.convert("11110-01-12")
