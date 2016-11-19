from collections import defaultdict

class WordCount:
    """
    This class allows you to count the total number of words, the total
    occurences of each of those words, and return a full list of the 
    words seen, sorted alphabetically and by popularity. 

    All words are stored in lowercase.
    Numbers are not included.
    """
    #_words_seen = defaultdict(int)
    #_word_counter = 0

    def __init__(self):
        self._words_seen = defaultdict(int)
        self._word_counter = 0     

    def reset(self):
        """This function resets the counter and words stored """
        self._words_seen = defaultdict(int)
        self._word_counter = 0

    def _file_reader(self, filename):
        """
        This function attempts to open a file from a given file
        name and returns the unfiltered list of words. 
        """
        try:
            text_file = open(filename, 'r')
            return text_file.read().split()

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
            self._words_seen[word] += 1
            self._word_counter += 1


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
        return self._word_counter

    def word_count(self, word):
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



