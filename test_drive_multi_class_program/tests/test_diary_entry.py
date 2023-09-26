from lib.diary_entry import *

def test_word_count():
    diary_entry = DiaryEntry("entry1", "entry2")
    assert diary_entry.count_words() == 1

def test_reading_time_as_words_per_minute():
    instance = DiaryEntry("title", "contents")
    result = instance.reading_time(1)
    assert result == 1

def test_reading_chunk():
    instance = DiaryEntry("title","one two three four")
    result = instance.reading_chunk(1, 1)
    assert result == 'one'

def test_reading_chunk_loops_back():
    instance = DiaryEntry("title","one two three four")
    instance.reading_chunk(1, 1)
    instance.reading_chunk(1, 1)
    instance.reading_chunk(1, 1)
    instance.reading_chunk(1, 1)
    result = instance.reading_chunk(1, 1)
    assert result == 'one'