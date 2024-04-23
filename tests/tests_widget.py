from src.widget import get_new_type_of_date, mask_card_or_account_number

print(mask_card_or_account_number("MasterCard 7158300734726758"))
print(mask_card_or_account_number("Visa Platinum 8990922113665229"))
print(mask_card_or_account_number("Счет 35383033474447895560"))
print(get_new_type_of_date("2018-07-11T02:26:18.671407"))
