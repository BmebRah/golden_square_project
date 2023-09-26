from lib.diary import * 
from lib.diary_entry import *
def test_number_of_words_returns_an_integer():
    instance = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    instance.add(entry_1)
    instance.add(entry_2)
    result = instance.count_words()
    assert result == 2