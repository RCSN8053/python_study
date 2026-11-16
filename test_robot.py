import pytest

from robot import can_deliver

def test_True():
    assert can_deliver(100, 5, 10 ) == True
def test_False():
    assert can_deliver(0, 5, 10 ) == False
def test_20():
    assert can_deliver(50, 3, 10 ) == True
def test_19():
    assert can_deliver(49, 3, 10) == False
def test_zero():
    assert can_deliver(40, 0, 4 ) == True
    