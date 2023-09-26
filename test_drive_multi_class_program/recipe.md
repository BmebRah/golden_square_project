1. Describe the Problem
Design single-class program

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

The interface of a class includes:

The name of the class.
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have
Steps 3 and 4 then operate as a cycle.

Example:

class TODO():
    def __init__(self, text, list):
parameters: text as string
            list 
def add_tak(self, text):
    returns: 
       string:  task added 
def remove_task():
    returns:
       string: task removed


3. Create Examples as Tests

These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.


# EXAMPLE

"""
Given a task as a string
It appends task to list and returns numbered string
"""
TODO.add_task("first_task") => 1, first_task

"""
Given empty string input 
It raises an Exception
"""
TODO.add_task("") =>  Exception raised "Empty string isnt valid input"

"""
Given a completed task it removes task and 
It returns string 

"""
Having added a list of completed task
It returns a list of tasks

"""
TODO.add_task("first_task") =>  removes task from list and returns string

"""
"""
Given a None value
It throws an error
"""
TODO.add_task(None) =>  Exception raised "None value isn't valid input"

Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour

For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.