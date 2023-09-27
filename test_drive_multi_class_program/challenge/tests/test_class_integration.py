from lib.todo import *
from lib.todo_list import *

def test_it_returns_a_list_of_incomplete_tasks():
    incomplete = TodoList()
    entry1 = Todo('task')
    incomplete.add(entry1)
    result = incomplete.incomplete()
    assert result == [entry1]

def test_it_returns_a_list_of_completed_tasks():
    completed = TodoList()
    entry2 = Todo('task')
    completed.add(entry2)
    result = completed.complete()
    assert result ==  [entry2]

def test_it_returns_all_todos_as_complete():
    all_complete = TodoList()
    entry3 = Todo('task')
    entry4 = Todo('task')
    all_complete.add(entry3)
    all_complete.add(entry4)
    result = all_complete.give_up()
    assert result == True