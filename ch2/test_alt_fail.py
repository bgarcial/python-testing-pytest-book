import pytest
from cards import Card

"""
A test will fail if there is any uncaught exception. This can happen if:
- an assert statement fails, which will raise an AssertionError exception,
- the test code calls pytest.fail(), which will raise an exception, or
- any other exception is raised.
While any exception can fail a test, I prefer to use assert. In rare cases where
assert is not suitable, use pytest.fail().
"""

def test_with_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    if c1 != c2:
        pytest.fail("they don't match")


"""
When calling pytest.fail() or raising an exception directly, we don’t get the won-
derful assert rewriting provided by pytest. However, there are reasonable
times to use pytest.fail(), such as in an assertion helper.
"""