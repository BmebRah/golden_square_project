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

def test_reading_time_for_all_entries():
    instance = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    instance.add(entry_1)
    instance.add(entry_2)
    result = instance.reading_time(1)
    assert result == 2

def test_find_best_entry_for_reading():
    instance = Diary()
    entry_1 = DiaryEntry("title", "contents contents")
    entry_3 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title2", "contents contents contents")
    instance.add(entry_1)
    instance.add(entry_3)
    instance.add(entry_2)
    result = instance.find_best_entry_for_reading_time(1,2)
    assert result == entry_2