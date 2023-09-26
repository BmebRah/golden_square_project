1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def starts_with_a_capital_letter_ends_with_suitable_punctuation(text):
    """returns first and last letters of a given text

    Parameters: (list all parameters and their types: text: string)
      words_in_text: number of words in text

    Returns: (state the return value and its type)
        Boolian

    Side effects: (state any side effects)
        
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.


# EXAMPLE

"""
Given a string of text with a upper case first letter and ends with a full stop
It returns True
"""
starts_with_a_capital_letter_ends_with_suitable_punctuation("the cat jumped on the table.") => True

"""
Given a string of text with a small cap first letter and ends with full stop
It returns False
"""
starts_with_a_capital_letter_ends_with_suitable_punctuation("hello world.") => Fasle 

"""

Given a string of text with a upper case first letter and ends with a colon
 tests_returns_false_if_first_character_is_not_upper_case_and_ends_with_a_
It return False
"""
starts_with_a_capital_letter_ends_with_suitable_punctuation("text:") => False
"""

Given an empty string
It returns None
"""
starts_with_a_capital_letter_ends_with_suitable_punctuation("") => None

"""

Given a None value
It throws an error
"""
starts_with_a_capital_letter_ends_with_suitable_punctuation(None) throws an error

Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a string of text
It returns first letter of text
"""
def test_starts_with_a_capital_letter_ends_with_suitable_punctuation():
    result =estimate_reading_time("hello WORLD")
    assert result == [hello, WORLD]
