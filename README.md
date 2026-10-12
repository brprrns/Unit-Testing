# Python Unit Testing Exercise

This project is about learning **Unit Testing, TDD, Mocking, and Code Coverage** using Python.

## Setup

First, install virtualenv:

```bash
pip install virtualenv
```

Create a virtual environment:

```bash
python -m virtualenv venv
```

Activate it:

### Windows

```bash
./venv/Scripts/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all the tests using:

```bash
pytest
```

or:

```bash
python -m pytest
```

## What I Learned

In this assignment, I learned about:

* Unit Testing
* TDD (Test Driven Development)
* Mocking
* Stubbing
* Pytest
* Moto for AWS testing
* Code Coverage

## Assignment Tasks

### 1. TDD

The tests were already provided in:

```text
tests/test_tdd_example.py
```

I completed the 4 methods in:

```text
src/tdd_example.py
```

The methods are:

* `reverse_string()`
* `find_longest_word()`
* `reverse_list()`
* `count_digits()`

### 2. General Unit Tests

I added unit tests for the methods in:

```text
src/general_example.py
```

For `fetch_emp_details()`, I used mocking for:

```text
load_employee_rec_from_database()
```

This prevents the test from accessing the actual database.

### 3. DynamoDB Tests

I completed the 3 tests in:

```text
tests/test_dynamodb_example.py
```

I used **Moto** to mock AWS DynamoDB.

### 4. Run Tests

All the test cases are run using Pytest.

### 5. Code Coverage

I generated a code coverage report to check how much of the code is covered by tests.


## Result

The required unit tests were implemented and the project was tested using Pytest.

The feature branch was pushed to the remote repository.

