from unittest import mock
import mod1
import mod2

def test_summer_a():
    with mock.patch("mod1.preamble", return_value = ""): #mod1.preamble is full name of the preamble() function in module mod1, return_value = "" is return empty string for this mock version
        assert "11" == mod2.summer(5,6)
        
def test_summer_b(): #almost the same with test_summer_a but it have mock object to interact
    with mock.patch("mod1.preamble") as moc_preamble:
        moc_preamble.return_value = ""
        assert "11" == mod2.summer(5,6)
        
@mock.patch("mod1.preamble", return_value ="")
def test_summer_c(mock_preamble):
    assert "11" == mod2.summer(5,6)

@mock.patch("mod1.preamble")
def test_caller_d(mock_preamble):
    mock_preamble.return_value = ""
    assert "11" == mod2.summer(5,6)

        