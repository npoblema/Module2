import pytest

from src.widget import masking_card_and_bill_numbers, convert_date


@pytest.mark.parametrize("info", "expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
])
def test_process_info(info, expected_result):
    assert masking_card_and_bill_numbers('')
