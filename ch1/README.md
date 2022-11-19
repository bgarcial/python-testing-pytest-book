# Executing tests command

- Executing one test individually, We can also specify a test function within a test file to run by adding ::test_name
to the file name:

```
> pytest -v test_one.py::test_passing
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book/ch1
collected 1 item                                                                                                                                 

test_one.py::test_passing PASSED                                                                                                           [100%]

=============================================================== 1 passed in 0.00s ================================================================
(pytest-book) 

```

- Specifying files and directories to test

>To run pytest, you have the option to specify files and directories. If you don’t specify any files or directories, pytest will look for tests in the current working directory and subdirectories. It looks for `.py` files starting with `test_` or ending with `_test`. 

>From the `ch1` directory, if you run `pytest` with no commands, you’ll run two files’ worth of tests:

`--tb=no` is to turn off tracebacks since we don’t really need
the full output right now.

```
/home/bgarcial/projects/python-testing-pytest-book/ch1 [git::main *] [bgarcial@skikk-NS5x-NS7xPU] [16:42]
> pytest -v --tb=no
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book/ch1
collected 2 items                                                                                                                                

test_one.py::test_passing PASSED                                                                                                           [ 50%]
test_two.py::test_failing FAILED                                                                                                           [100%]

============================================================ short test summary info =============================================================
FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
========================================================== 1 failed, 1 passed in 0.00s ===========================================================
```

- Specifying files 

We can also get the same set of tests to run by specifying them 

```
/home/bgarcial/projects/python-testing-pytest-book/ch1 [git::main *] [bgarcial@skikk-NS5x-NS7xPU] [16:42]
> pytest -v --tb=no test_one.py test_two.py 
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book/ch1
collected 2 items                                                                                                                                

test_one.py::test_passing PASSED                                                                                                           [ 50%]
test_two.py::test_failing FAILED                                                                                                           [100%]

============================================================ short test summary info =============================================================
FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
========================================================== 1 failed, 1 passed in 0.00s ===========================================================
(pytest-book) 

```    

- or by listing the directory name:

```
/home/bgarcial/projects/python-testing-pytest-book [git::main *] [bgarcial@skikk-NS5x-NS7xPU] [16:50]
> pytest -v --tb=no ch1/                    
============================================================== test session starts ===============================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/bgarcial/projects/python-testing-pytest-book
collected 2 items                                                                                                                                

ch1/test_one.py::test_passing PASSED                                                                                                       [ 50%]
ch1/test_two.py::test_failing FAILED                                                                                                       [100%]

============================================================ short test summary info =============================================================
FAILED ch1/test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
========================================================== 1 failed, 1 passed in 0.00s ===========================================================

```

---

 
# Test Discovery and Naming conventions

>The part of pytest execution where pytest goes off and finds which tests to run is called test discovery. pytest was able to find all the tests we wanted it to run because we named them according to the pytest naming conventions.
Given no arguments, pytest looks at your current directory and all subdirectories for test files and runs the test code it finds. If you give pytest a filename, a directory name, or a list of those, it looks there instead of the current directory. Each directory listed on the command line is examined for test code, as well as any subdirectories.

>Here’s a brief overview of the naming conventions to keep your test code discoverable by pytest:

- Test files should be named `test_<something>.py` or `<something>_test.py`.

- Test methods and functions should be named `test_<something>`.

- Test classes should be named `Test<Something>`.


---

# Test Outcomes

So far we’ve seen one passing test and one failing test. However, pass and fail are not the only outcomes possible.
Here are the possible outcomes of a test:

Here are the possible outcomes of a test:

- PASSED (.)—The test ran successfully.

- FAILED (F)—The test did not run successfully.

- SKIPPED (s)—The test was skipped. You can tell pytest to skip a test by using either the `@pytest.mark.skip()` or `@pytest.mark.skipif()` decorators, which are discussed in Skipping Tests with `pytest.mark.skip`, on page 74.

- XFAIL (x)—The test was not supposed to pass, and it ran and failed. You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator, which is discussed in Expecting Tests to Fail with `pytest.mark.xfail`, on page 77.

    When you do this you will see:
    ```
    > pytest -v --tb=no ch1
    ============================================================== test session starts ===============================================================
    platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /home/bgarcial/.pyenv/versions/3.10.8/envs/pytest-book/bin/python3.10
    cachedir: .pytest_cache
    rootdir: /home/bgarcial/projects/python-testing-pytest-book
    collected 2 items                                                                                                                                

    ch1/test_one.py::test_passing PASSED                                                                                                       [ 50%]
    ch1/test_two.py::test_failing XFAIL                                                                                                        [100%]

    ========================================================== 1 passed, 1 xfailed in 0.00s ==========================================================
    ``` 

- XPASS (X)—The test was marked with xfail, but it ran and passed.

- ERROR (E)—An exception happened either during the execution of a fixture or hook function, and not during the execution of a test function. Fixtures are discussed in Chapter 3, pytest Fixtures, on page 31, and hook functions are discussed in Chapter 15, Building Plugins, on page 205.