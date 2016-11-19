from collections import defaultdict

class WordCount:
    """
    This class allows you to count the total number of words, the total
    occurences of each of those words, and return a full list of the 
    words seen. All words are stored in lowercase.
    """
    _words_seen = defaultdict[int]
    _word_counter = 0

    def reset(self):
        """This function resets the counter and words stored """
        self._words_seen = defaultdict[int]
        self._word_counter = 0

    def _file_reader(self, filename):
        """
        This function attempts to open a file from a given file
        name and count the contained words. 
        """
        file = open(filename, 'r')

        return

    def _word_cleaner(self, word):
        """ 
        This function strips the words of capitalization and 
        punctuation, if necessary.
        """
        return

    def _add_to_count(self, word):
        """This function increments the overall and dictionary counts."""
        self._words_seen[word] += 1
        self._word_counter += 1


    def word_count_total(self):
        """This function returns the current total word count. """
        return _word_counter

    def word_count_specific(self, word):
        """This function returns the current count for a given word."""
        clean_word = self._word_cleaner(word)
        return self._words_seen[clean_word]

    def words_list_alphabetical(self):
        """
        This function returns a list of all the words seen, sorted 
        alphabetically.
        """
        return

    def words_list_rank(self):
        """
        This function returns a list of lists of the words seen, 
        sorted by their respective number of appearences.
        """
        return



