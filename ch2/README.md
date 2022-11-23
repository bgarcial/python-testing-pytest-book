In our case, the Cards project is the application code. It is an installable Python package, and we need to install it in order to test it. Installing it will also allow us to play with the Cards project on the command line. If the code you are testing is not a Python package that can be installed, you’ll have to use other ways to get your test to see your code. (Some alternatives are discussed in Chapter 12, Testing Scripts and Applications, on page 165.)


If you haven’t already done so, you can download a copy of the source code
for this project from the book’s web page.1 Download and unzip the code to
a location on your computer you are comfortable working with and can find
easily later. For the rest of the book, I’ll be referring to this location as `path/to/code`. The Cards project is at `/path/to/code/cards_project`, and the tests for this chapter are at /path/to/code/ch2.


# Testing

These tests are intended to demonstrate how to use a data structure. They aren’t exhaustive
tests; they are not looking for corner cases, or failure cases, or looking for ways to make 
the data structure blow up. I haven’t tried passing in gibberish or negative numbers as IDs 
or huge strings. That’s not the point of this set of tests



```
> pytest -v ch2/test_card.py::test_field_access
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book
collected 1 item                                                                                                                                 

ch2/test_card.py::test_field_access PASSED                                                                                                 [100%]

=============================================================== 1 passed in 0.02s ================================================================
```

```
> pytest -v ch2/test_card.py
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book
collected 7 items                                                                                                                                

ch2/test_card.py::test_field_access PASSED                                                                                                 [ 14%]
ch2/test_card.py::test_defaults PASSED                                                                                                     [ 28%]
ch2/test_card.py::test_equality PASSED                                                                                                     [ 42%]
ch2/test_card.py::test_equality_with_diff_ids PASSED                                                                                       [ 57%]
ch2/test_card.py::test_inequality PASSED                                                                                                   [ 71%]
ch2/test_card.py::test_from_dict PASSED                                                                                                    [ 85%]
ch2/test_card.py::test_to_dict PASSED                                                                                                      [100%]

=============================================================== 7 passed in 0.03s ================================================================
```

>The point of these tests is to check my understanding of how the structure
works, and possibly to document that knowledge for someone else or even
for a future me. This use of checking my own understanding, and really of
using tests as little playgrounds to play with the application code, is super
powerful, and I think more people would enjoy testing more if they start with
this mindset.

# Using assert Statements
When you write test functions, the normal Python assert statement is your
primary tool to communicate test failure. The simplicity of this within pytest
is brilliant. It’s what drives a lot of developers to use pytest over other
frameworks.

If you’ve used any other testing framework, you’ve probably seen various assert
helper functions. For example, following is a list of a few of the assert forms
and assert helper functions from unittest:

| pytest                 |      unittest                   | 
|------------------------|:-------------------------------:|
| `assert something`     | `assertTrue(something)`         | 
| `assert not something` |    `assertFalse(something)`     |  
| `assert a == b`        | `assertEqual(a, b)`             |    
| `assert a != b`        | `assertNotEqual(a, b)`          |
| `assert a is None`     | `assertIsNone(a)`               |
| `assert a is not None` | `assertIsNotNone(a)`            |
| `assert a <= b`        | `assertLessEqual(a, b)`         |

---

With pytest, you can use assert <expression> with any expression. If the expres-
sion would evaluate to False if converted to a bool, the test would fail.

`pytest` includes a feature called “assert rewriting” that intercepts assert calls
and replaces them with something that can tell you more about why your
assertions failed. Let’s see how helpful this rewriting is by looking at an
assertion failure:

```
def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")
    assert c1 == c2
```

Just for reference, we can see what Python gives us by default for assert failures.
We can run the test, not from pytest, but directly from Python by adding
a  `if __name__ == '__main__'` block at the end of the file and calling `test_equality_fail()`,
like this:

```
if __name__ == "__main__":
    test_equality_fail()
```

Using `if __name__ == '__main__'` is a quick way to run some code from a file but
not allow the code to be run if it is imported. When a module is imported,
Python will fill in `__name__` with the name of the module, which is the name of
the file without the `.py`. However, if you run the file with `python file.py`, `__name__`
will be filled in by Python with the string `"__main__"`.

---
# Writing Assertion Helper Functions

An assertion helper is a function that is used to wrap up a complicated
assertion check. As an example, the Cards data class is set up **such that two
cards with different IDs will still report equality.** If we wanted to have a stricter
check, we could write a helper function called assert_identical like this: see `test_helper.py` file

---

# Testing for Expected Exceptions

We’ve looked at how any exception can cause a test to fail. But what if a bit
of code you are testing is supposed to raise an exception? How do you test
for that?
You use `pytest.raises()` to test for expected exceptions.

As an example, the cards API has a CardsDB class that requires a path argument.
What happens if we don’t pass in a path? Let’s try it:

```
import cards

def test_no_path_fail():
    cards.CardsDB()
```

Then test it 
```
> pytest --tb=short ch2/test_experiment.py::test_no_path_fail
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/bgarcial/projects/python-testing-pytest-book
collected 1 item                                                                                                                                 

ch2/test_experiment.py F                                                                                                                   [100%]

==================================================================== FAILURES ====================================================================
_______________________________________________________________ test_no_path_fail ________________________________________________________________
ch2/test_experiment.py:4: in test_no_path_fail
    cards.CardsDB()
E   TypeError: CardsDB.__init__() missing 1 required positional argument: 'db_path'
============================================================ short test summary info =============================================================
FAILED ch2/test_experiment.py::test_no_path_fail - TypeError: CardsDB.__init__() missing 1 required positional argument: 'db_path'
=============================================================== 1 failed in 0.05s ================================================================
```

Here the `--tb=short` shorter traceback format is used because we don’t need to
see the full traceback to find out which exception is raised.

The `TypeError` exception seems reasonable, since the error occurs when trying
to initialize the custom CardsDB type. See `/home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/lib/python3.10/site-packages/cards/api.py` internal file:

![](https://cldup.com/zr0vBRlHp6.png)

When trying to initialize the custom `CardsDB` type,it needs a `db_path argument that is missing and that is why the
`TypeError` exception raised. We can write a test to make sure this exception is thrown, like this:

```
import pytest
import cards


def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()
```

The `with pytest.raises(TypeError):` statement says that whatever is in the next block
of code should raise a `TypeError` exception. If no exception is raised, the test
fails. If the test raises a different exception, it fails.

```
> pytest --tb=short ch2/test_exceptions.py::test_no_path_raises
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/bgarcial/projects/python-testing-pytest-book
collected 1 item                                                                                                                                 

ch2/test_exceptions.py .                                                                                                                   [100%]

=============================================================== 1 passed in 0.02s ================================================================

```
