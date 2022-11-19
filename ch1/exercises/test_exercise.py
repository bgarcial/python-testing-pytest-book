import pytest

@pytest.mark.xfail()
def test_evaluate_numbers():
    list = [2,3,4]
    assert 1 in list


def test_evaluate_letters():
    a = 0
    b = 1
    assert a < b


@pytest.mark.xfail()
def test_evaluate_contains():
    assert 'fizz' not in 'fizzbuzz'