import math
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title=title
        self.contents=contents
        self.total_words_read = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        words = math.ceil(self.count_words() / wpm)
        return words

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words_user_can_read = wpm * minutes
        split_words = self.contents.split(" ")
        if self.total_words_read == len(split_words):
            self.total_words_read = 0
        ending = self.total_words_read + words_user_can_read
        start = self.total_words_read
        self.total_words_read += words_user_can_read
        return " ".join(split_words[start:ending])