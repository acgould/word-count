# implementation of the WordCount class

from collections import defaultdict

class WordCount:
    """
    This class allows you to count the total number of words, the total
    occurences of each of those words, and return a full list of the 
    words seen, sorted alphabetically and by popularity. 

    All words are stored in lowercase.
    """

    def __init__(self):
        self._word_counts = defaultdict(int)
        self._total_words = 0     

    def reset(self):
        """This function resets the counter and words stored """
        self._word_counts = defaultdict(int)
        self._total_words = 0

    def _file_reader(self, filename):
        """
        This function attempts to open a file from a given file
        name and returns the unfiltered list of words. 
        """
        try:
            text_file = open(filename, 'r')
            words = text_file.read().split()
            text_file.close()
            return words

        except NameError: # in case there is a problem with the file name
            print("No such file " + filename + " found.")
            return False

    def _word_cleaner(self, word):
        """ 
        This function strips the words of capitalization and 
        punctuation, if necessary. 
        Note: Plural posessives which end in an apostrophe will be 
        stripped of that character, as will contractions beginning with
        an apostrophe.
        Note: This implementation uses str.lstrip() and str.rstrip() with 
        given sets of non-alpha chars.
        """
        #strip leading and trailing punctuation
        punctuation = '\"\',.!?<>()[]:;-_*&#$%@^'
        word = word.lstrip(punctuation)
        word = word.rstrip(punctuation)
        #convert to lowercase
        word = word.lower()
        return word


    def _add_to_count(self, word):
        """This function increments the overall and dictionary counts."""
        if len(word) > 0:
            self._word_counts[word] += 1
            self._total_words += 1

    def _words_list_sort(self):
        """
        This function returns a defaultdict(list) of the words seen, 
        grouped by their respective number of appearences.
        """
        rank_dict = defaultdict(list)
        # for all the words we have seen, add to new dict w/ count as key
        for word, count in self._word_counts.items():
            rank_dict[count] += [word]
        return rank_dict

    def _per(self, count):
        """ This function returns count/total count"""
        return float(count)/self._total_words


    # Functions for public use

    def count_file(self, filename):
        """
        This function adds all the words in the file given to the 
        current count. Note: does not automatically reset count.
        """
        list_of_words = self._file_reader(filename)
        for word in list_of_words:
            self._add_to_count(self._word_cleaner(word))


    def word_count_total(self):
        """This function returns the current total word count. """
        return self._total_words

    def word_count(self, word):
        """This function returns the current count for a given word."""
        clean_word = self._word_cleaner(word)
        return self._word_counts[clean_word]

    def words_alphabetical(self):
        """
        This function returns a list of all the words seen, sorted 
        alphabetically.
        """
        return sorted(self._word_counts.keys())

    def words_ranked(self):
        """
        This function returns a list of tuples, where each tuple contains
        (frequency, [list of words]).
        """
        # get our dictionary of words organized by rank
        rank_dict = self._words_list_sort()
        # get the keys, sorted in decending order
        counts = sorted(rank_dict.keys(), reverse = True)
        # return a list of tuples (count, list of words)
        return [ (c, sorted(rank_dict[c])) for c in counts]

    def words_percent(self):
        """
        This function returns a list of tuples, where each tuple contains
        (frequency percentage, [list of words]).
        """
        # get our dictionary of words organized by rank
        rank_dict = self._words_list_sort()
        # get the keys, sorted in decending order
        counts = sorted(rank_dict.keys(), reverse = True)
        # return a list of tuples (count, list of words)
        return [ (self._per(c), sorted(rank_dict[c])) for c in counts]

    def word_stats(self):
        """
        This function returns a list of tuples, where each tuple contains
        (count, frequency percentage, [list of words]).
        """
        # get our dictionary of words organized by rank
        rank_dict = self._words_list_sort()
        # get the keys, sorted in decending order
        counts = sorted(rank_dict.keys(), reverse = True)
        # return a list of tuples (count, list of words)
        return [ (c, self._per(c), sorted(rank_dict[c])) for c in counts]







