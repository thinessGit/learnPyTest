import pytest

def test_evenNo():
    num = 6
    assert (num % 2) == 0

def test_ture():
    assert True

@pytest.mark.xfail
def test_false():
    assert False, " Testcase failed "
