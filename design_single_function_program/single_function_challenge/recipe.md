1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def text_incudes(text):
    """return Boolean True/Fasle

    Parameters: (text)

    Returns:
        True/ False
 
    Side effects: (state any side effects)
        
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.


# EXAMPLE

"""
Given a string of with small case todo
It returns False
"""
text_includes("the todo list") => False

"""
Given a string of mixed cases todo 
It returns False
"""
text_includes("the toDO list") => False

"""
Given a string of text with upper case todo
It returns True
"""
text_includes("the TODO list") => True

"""
Given no text
It throws an error
"""
text_includes() => error

"""
Given a None value
It throws an error
"""
text_includes(None) throws an error

Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a string of text
It returns a list of comma delimited words
"""
def test_returns_a_list_of_comma_delimited_words():
    result =estimate_reading_time("hello WORLD")
    assert result == [hello, WORLD]
