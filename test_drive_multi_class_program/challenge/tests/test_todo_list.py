from lib.todo_list import *

def test_it_adds_instance_of_todo():
    todo_instance = TodoList()
    todo_entry = todo_instance.add('task')
    assert todo_entry == ['task']

    