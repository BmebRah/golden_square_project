
from lib.diary import *
def test_diary_instantiates_with_init():
    instatiate = Diary()
    assert instatiate.my_list == []
def test_adds_entry():
    instance = Diary()
    instance.add('my_entry')
    assert instance.my_list[0] == "my_entry"
def test_it_returns_a_list_of_instances():
    instance = Diary()
    instance.add('my_entry')
    result = instance.all()
    assert result == ["my_entry"]

