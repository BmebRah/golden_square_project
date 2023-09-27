from lib.todo import *
def test_it_instantiates_with_init_attributes():
    complete_instance = Todo('task')
    assert complete_instance.complete == False

def test_it_sets_complete_property_to_true():
    task_completed = Todo('task')
    assert task_completed.mark_complete() == True