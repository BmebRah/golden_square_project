class Diary:
    def __init__(self):
        self.my_list=[]

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.my_list.append(entry)


    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.my_list

    def count_words(self):
        total_count = 0
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        for item in self.my_list:
            total_count+= item.count_words()
        return total_count
            

    def reading_time(self, wpm):
        total_reading_time = 0
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        for item in self.my_list:
            total_reading_time += item.reading_time(wpm)
        
        return total_reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        entry_within_minutes = [item for item in self.my_list if item.reading_time(wpm) <= minutes]
        # print([i.reading_time(wpm) for i in entry_within_minutes])
        best_entry = max(entry_within_minutes, key = lambda item: item.reading_time(wpm))
        return best_entry