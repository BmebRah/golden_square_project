1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def estimate_reading_time(text):
    """return how many words can a user read in a given text at 200/minute speed

    Parameters: (list all parameters and their types: words:'string', text:list)
      words_in_text: number of words in text

    Returns: (state the return value and its type)
        int 
 
    Side effects: (state any side effects)
        
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.


# EXAMPLE

"""
Given a string of text 
It returns comma delimited words
"""
estimate_reading_time("the cat jumped on the table") => the cat jumped on the table

"""
Given a string of text
It returns length of text
"""
estimate_reading_time("text") => 4

"""
Given a string of text
It returns length of text ignoring spaces in between for accurate calculation
"""
estimate_reading_time("hello world") => 10 

"""
Given no text
It returns None
"""
estimate_reading_time() => None

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error

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
