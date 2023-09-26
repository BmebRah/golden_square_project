from lib.starts_with_capital_letter_ends_with_suitable_punctuation_mark import *

def tests_returns_true_if_first_character_is_upper_case_ends_with_a_full_stop():
    first_letter = starts_with_capital_letter_ends_with_suitable_punctuation('Text.')
    assert first_letter == True
def tests_returns_false_if_first_character_is_not_upper_case_and_ends_with_an_excalmation_mark():
    exclamation_mark = starts_with_capital_letter_ends_with_suitable_punctuation('text!')
    assert exclamation_mark == False
def tests_returns_false_if_first_character_is_not_upper_case_and_ends_with_a_colon():
    colon = starts_with_capital_letter_ends_with_suitable_punctuation('text:')
    assert colon == False
def tests_returns_false_if_first_character_is_not_upper_case_and_ends_with_a_full_stop():
    result = starts_with_capital_letter_ends_with_suitable_punctuation('text.')
    assert result == False

