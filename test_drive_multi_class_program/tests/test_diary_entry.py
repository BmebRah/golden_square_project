from lib.diary_entry import *

def test_word_count():
    diary_entry = DiaryEntry("entry1", "entry2")
    assert diary_entry.count_words() == 1
def test_reading_time_as_words_per_minute():
    