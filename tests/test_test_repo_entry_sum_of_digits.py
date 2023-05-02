from test_repo.entry import sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(555) == 15
    assert sum_of_digits(999999) == 54