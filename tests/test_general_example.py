from unittest.mock import patch

from src.general_example import GeneralExample


def test_flatten_dictionary():
    data = {
        'key1': [3, 2, 1],
        'key2': [42, 55, 10],
        'key3': [0, 22]
    }

    expected = [0, 1, 2, 3, 10, 22, 42, 55]

    actual = GeneralExample.flatten_dictionary(data)

    assert actual == expected


@patch.object(
    GeneralExample,
    'load_employee_rec_from_database'
)
def test_fetch_emp_details(mock_load_employee):
    mock_load_employee.return_value = [
        'emp001',
        'Sam',
        '100000'
    ]

    general_example = GeneralExample()

    expected = {
        'empId': 'emp001',
        'empName': 'Sam',
        'empSalary': '100000'
    }

    actual = general_example.fetch_emp_details()

    assert actual == expected
    mock_load_employee.assert_called_once()