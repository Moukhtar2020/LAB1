import pytest
import main
import math
import pytest_cov
import pytest

@pytest.mark.parametrize(
"principal, annualInterestRate, termInYears, expected",
[
pytest.param(-1, 12, 16, "Principal must be a positive number", id='minMinusP'),
pytest.param(0, 12, 10, 0.0, id='minP'),
pytest.param(1, 12, 10, 0.014115298423584444, id='minPlusP'),
pytest.param(5000, 12, 10, 70.57, id='nomP'),
pytest.param(999999999, 12, 10, 14115298.40, id='maxMinusP'),
pytest.param(1000000000, 12, 10, 14115298.42, id='maxP'),
pytest.param(1000000001, 12, 10, "Principal must be less than a billion", id='maxPlusP'),
pytest.param(82, -1, 10, "Annual interest rate must be a positive number", id='minMinusA'),
pytest.param(83, 0, 10, 0.68, id='minA'),
pytest.param(84, 1, 10, 0.72, id='minPlusA'),
pytest.param(85, 12, 10, 1.19, id='nomA'),
pytest.param(86, 24, 10, 1.86, id='maxMinusA'),
pytest.param(87, 25, 10, 1.94, id='maxA'),
pytest.param(90, 26, 10, "Rate must be between 0 and 25", id='maxPlusA'),
pytest.param(90, 20, 0, "Term in years must be a positive number greater than zero", id='minMinusT'),
pytest.param(90, 20, 1, 8.16, id='minT'),
pytest.param(90, 20, 2, 4.48, id='minPlusT'),
pytest.param(90, 20, 20, 1.50, id='nomT'),
pytest.param(90, 20, 39, 1.48, id='maxMinusT'),
pytest.param(90, 20, 40, 1.47, id='maxT'),
pytest.param(90, 20, 41, "Term in years must be less than 40 years", id='maxPlusT'),
]
)

def test_calculate_mortgage_payment(principal, annualInterestRate, termInYears, expected):
    try:
        actual_payment = main.calculate_mortgage_payment(
            principal, annualInterestRate, termInYears
        )
        assert pytest.approx(actual_payment, 0.01) == expected
    except ValueError as e:
        assert str(e) == expected
