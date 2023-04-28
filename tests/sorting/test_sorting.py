from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock_data = [
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "25-06-22"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "25-06-22"},
    ]

    expect_result = [
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "25-06-22"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "25-06-22"},
    ]

    sort_by(mock_data, "max_salary")

    assert mock_data == expect_result
