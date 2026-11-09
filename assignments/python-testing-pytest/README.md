# 📘 Assignment: Testing Python Functions with pytest

## 🎯 Objective

Write and run automated tests with pytest to check Python functions. Practice using assertions and choosing normal and edge-case inputs to catch mistakes.

## 📝 Tasks

### 🛠️ Run the Starter Test

#### Description
Install pytest, run the provided test, and see how a passing test confirms a function's behavior.

#### Requirements
Completed program should:

- Install pytest with `python -m pip install pytest`
- Run the tests with `python -m pytest -q`
- Confirm the provided test passes without changing `functions.py`


### 🛠️ Test Even and Odd Numbers

#### Description
Add tests for `is_even()` to check its behavior with even, odd, zero, and negative numbers.

#### Requirements
Completed program should:

- Add at least three tests to `test_functions.py`
- Use `assert` to check the expected result for each input
- Include at least one even number, one odd number, zero, and one negative number across the tests


### 🛠️ Test Names and Totals

#### Description
Write tests for `format_name()` and `calculate_total()` using typical inputs and edge cases.

#### Requirements
Completed program should:

- Check that `format_name()` trims extra spaces and formats names consistently
- Check that `calculate_total()` returns the sum of multiple values and returns `0` for an empty list
- Run `python -m pytest -q` and confirm all tests pass without changing `functions.py`