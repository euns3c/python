import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

s = "안녕하세요"

def test_string():
    assert s == "안녕하세요"
