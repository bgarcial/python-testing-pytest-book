import pytest
import cards


def test_no_path_raises():
    """
    The `with pytest.raises(TypeError):` statement says that whatever is in the next block
    of code should raise a `TypeError` exception. If no exception is raised, the test
    fails. If the test raises a different exception, it fails.
    """
    with pytest.raises(TypeError):
        cards.CardsDB()


def test_raises_with_info():
    """
    We can also check to make sure the message is correct, or any other aspect of the exception, 
    like additional parameters:
    """
    match_regex = "missing 1 .* positional argument"

    # The `match` parameter takes a regular expression and matches it with the exception message.
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exec_info:
        cards.CardsDB()
    expected = "missing 1 required positional argument"
    """
    You can also use as exc_info or any other variable name to
    interrogate extra parameters to the exception if it’s a custom exception
    The `exc_info` object will be of type ExceptionInfo 
    - https://docs.pytest.org/en/latest/reference/reference.html#exceptioninfo
    """
    assert expected in str(exec_info)
