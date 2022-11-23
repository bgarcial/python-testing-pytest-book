from cards import Card
import pytest


# Helper function, two cards with different IDs will still report equality. 
def assert_identical(c1: Card, c2: Card):
    # __tracebackhide__ = True
    # This is optional. The effect will be that failing tests will not include 
    # this function in the traceback
    assert c1 == c2
    # also used assert c1.id == c2.id, "id's don't match."
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")


def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)
    assert_identical(c1, c2)


def test_identical_fail():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=456)
    assert_identical(c1, c2)