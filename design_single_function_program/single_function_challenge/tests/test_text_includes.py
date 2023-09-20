import pytest
from lib.text_includes import *
# Given a string of with small case todo
# It returns False

def test_text_includes_small_case_todo_string():
    small_case_todo = text_includes('todo')
    assert small_case_todo == False

# Given a string of mixed cases todo 
# It returns False

def test_text_contains_mixed_case_todo_string():
    mixed_case_todo = text_includes('toDO')
    assert mixed_case_todo == False

# Given a string of text with upper case todo
# It returns True

def test_text_contains_upper_case_todo_string():
    upper_case_todo = text_includes('TODO')
    assert upper_case_todo == True

# Given no text
# It throws an error

def test_no_text_was_passed_to_function():
    with pytest.raises(Exception) as e:
        text_includes("")
    error_message = str(e.value)
    assert error_message == 'No Text Passed'

# Given a None value
# It throws an error

def test_none_value_passed_as_parameter():
    with pytest.raises(Exception) as e:
            text_includes(None)
    error_message = str(e.value)
    assert error_message == "'NoneType' object is not iterable"