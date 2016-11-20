
# file to test wordcount class in wordcount.py

from wordcount import WordCount

def list_of_strings(length):
    """This function creates a list of strings to aid testing,"""
    list = range(length)
    for i in range(length):
        list[i] = str(i)
    return list

def test_file_to_words(file):
    """
    This tests that the file properly opens and returns a list of the words
    without spaces or new lines.
    """
    wc = WordCount()
    return wc._file_reader(file)

def all_test_file_to_words():
    print "Testing ability to open file and return words: "
    assert test_file_to_words('blank.txt') == []
    print test_file_to_words('words.txt')
    print test_file_to_words('wordswithcaps.txt')
    print test_file_to_words('wordswithpunct.txt')
    print test_file_to_words('wordswithnewlines.txt')
    print test_file_to_words('wordswithdupfreqs.txt')

def test_clean_words(list):
    wc = WordCount()
    for i in range(len(list)):
        list[i] = wc._word_cleaner(list[i])
    return list

def all_test_clean_words():
    print "Testing ability to clean words."
    clean_list = ['a', 'b', 'c', 'd']
    assert test_clean_words([]) == []
    assert test_clean_words(['a', 'b', 'c', 'd']) == clean_list
    assert test_clean_words(['A', 'B', 'C', 'D']) == clean_list
    assert test_clean_words(['a.', 'b,', 'c?', 'd!']) == clean_list
    assert test_clean_words(['"a', 'b"', '"(c', 'd!"']) == clean_list
    assert test_clean_words(['$%^^&*a', '!!!b!!!', 'c)))', 'd-']) \
            == clean_list
    assert test_clean_words(['Hello!']) == ['hello']
    assert test_clean_words(["Don't!!"]) == ["don't"]

def test_reset(num, list_of_words):
    wc1 = WordCount()
    wc2 = WordCount()

    # increase wc1
    wc1._total_words += num
    for word in list_of_words:
        wc1._word_counts[word] += 1

    # check that they are now different
    if num > 0:
        assert wc1._total_words > wc2._total_words
    if len(list_of_words) > 0:
        assert len(wc1._word_counts.items()) > len(wc2._word_counts.items())

    #reset
    wc1.reset()

    # check that wc1 has indeed reset
    assert wc1._total_words == wc2._total_words
    assert wc1._total_words == 0
    assert len(wc1._word_counts.items()) == len(wc2._word_counts.items())
    assert len(wc1._word_counts.items()) == 0

def all_test_reset():
    print "Testing proper reset."
    test_reset(1, ['hi'])
    test_reset(4, ['a', 'b', 'c', 'd'])
    test_reset(500, list_of_strings(1000))

def test_add(list_of_words):
    wc = WordCount()
    manual_count = 0
    for word in list_of_words:
        wc._add_to_count(word)
        manual_count += 1
        assert wc._word_counts[word] > 0
        assert wc._total_words == manual_count

def all_test_add():
    print "Testing addition of words to increase counts."
    test_add([])
    test_add(['a', 'b', 'c', 'd'])
    test_add(list_of_strings(100))
    test_add(list_of_strings(100) + list_of_strings(200))

def test_count_file(filename):
    """ This test only works for my numeric-based test files. """
    wc = WordCount()
    wc.count_file(filename)
    assert wc._total_words == 10
    assert wc._word_counts['zero'] == 0
    assert wc._word_counts['one'] == 1
    assert wc._word_counts['two'] == 2
    assert wc._word_counts['three'] == 3
    assert wc._word_counts['four'] == 4

def all_test_count_file():
    print "Testing addition of files to increase counts."
    test_count_file('words.txt')
    test_count_file('wordswithcaps.txt')
    test_count_file('wordswithpunct.txt')
    test_count_file('wordswithnewlines.txt')   

def test_count_mult_files(list_of_filenames):
    wc = WordCount()
    mult = 1
    for file in list_of_filenames:
        wc.count_file(file)
        assert wc._total_words == 10*mult
        assert wc._word_counts['zero'] == 0
        assert wc._word_counts['one'] == 1*mult
        assert wc._word_counts['two'] == 2*mult
        assert wc._word_counts['three'] == 3*mult
        assert wc._word_counts['four'] == 4*mult
        mult += 1

def all_test_count_mult_files():
    print "Testing addition of multiple files to up counts w/o reset."
    all_files = ['words.txt', 'wordswithcaps.txt', 'wordswithpunct.txt', \
        'wordswithnewlines.txt']
    test_count_mult_files(all_files[:1])
    test_count_mult_files(all_files[:2])
    test_count_mult_files(all_files[:3])
    test_count_mult_files(all_files[:4])
    test_count_mult_files(all_files)    

def test_word_count_total(list_of_words):
    wc = WordCount()
    manual_count = 0
    for word in list_of_words:
        wc._add_to_count(word)
        manual_count += 1
        assert wc.word_count_total() == manual_count
        assert wc.word_count_total() == wc._total_words

def all_test_word_count_total():
    print "Testing proper return of total word count."
    test_word_count_total([])
    test_word_count_total(list_of_strings(100))
    test_word_count_total(list_of_strings(1000))
    test_word_count_total(list_of_strings(1000) + list_of_strings(1000))

def test_word_count_unique(list_of_words):
    wc = WordCount()
    for word in list_of_words:
        wc._add_to_count(word)
    return wc.word_count_unique()

def all_test_word_count_unique():
    print "Testing proper return of unique words count."
    assert test_word_count_unique([]) == 0
    assert test_word_count_unique(list_of_strings(100)) == 100
    assert test_word_count_unique(list_of_strings(1000)) == 1000
    assert test_word_count_unique(list_of_strings(1000) \
        + list_of_strings(1000)) == 1000
    assert test_word_count_unique(list_of_strings(100) + list_of_strings(50) \
        + list_of_strings(25)) == 100

def test_alpha_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_alphabetical()


def all_test_alpha_words():
    print "Testing proper return of all words alphabetically."
    alpha_list = ['four', 'one', 'three', 'two']
    assert test_alpha_words('blank.txt') == []
    assert test_alpha_words('words.txt') == alpha_list
    assert test_alpha_words('wordswithcaps.txt') == alpha_list
    assert test_alpha_words('wordswithpunct.txt') == alpha_list
    assert test_alpha_words('wordswithnewlines.txt') == alpha_list
    alpha_num_list = ['1', '2', '3', '4', 'cuatro', 'dos', 'four', 'one', \
        'three', 'tres', 'two', 'uno']
    assert test_alpha_words('wordswithdupfreqs.txt') == alpha_num_list

def test_ranked_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_ranked()

def all_test_ranked_words():
    print "Testing proper return of all words and frequencies ranked."
    alpha_list = [(4, ['four']), (3, ['three']), (2, ['two']), (1, ['one'])]
    assert test_ranked_words('blank.txt') == []
    assert test_ranked_words('words.txt') == alpha_list
    assert test_ranked_words('wordswithcaps.txt') == alpha_list
    assert test_ranked_words('wordswithpunct.txt') == alpha_list
    assert test_ranked_words('wordswithnewlines.txt') == alpha_list   
    alpha_num_list = [(4, ['4', 'cuatro', 'four']), \
        (3, ['3', 'three', 'tres']), (2, ['2', 'dos', 'two']), \
        (1, ['1', 'one', 'uno'])]
    assert test_ranked_words('wordswithdupfreqs.txt') == alpha_num_list

def test_perc_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_percent()

def all_test_perc_words():
    print "Testing proper return of all words and frequencies ranked."
    alpha_list = [(0.4, ['four']), (0.3, ['three']), (0.2, ['two']), \
        (0.1, ['one'])]
    assert test_perc_words('blank.txt') == []
    assert test_perc_words('words.txt') == alpha_list
    assert test_perc_words('wordswithcaps.txt') == alpha_list
    assert test_perc_words('wordswithpunct.txt') == alpha_list
    assert test_perc_words('wordswithnewlines.txt') == alpha_list   
    alpha_num_list = [(4.0/30, ['4', 'cuatro', 'four']), \
        (3.0/30, ['3', 'three', 'tres']), (2.0/30, ['2', 'dos', 'two']), \
        (1.0/30, ['1', 'one', 'uno'])]
    assert test_perc_words('wordswithdupfreqs.txt') == alpha_num_list

def test_words_stats(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.word_stats()

def all_test_words_stats():
    print "Testing proper return of words, counts, and percentages, ranked."
    alpha_list = [(4, 0.4, ['four']), (3, 0.3, ['three']), \
        (2, 0.2, ['two']), (1, 0.1, ['one'])]
    assert test_words_stats('blank.txt') == []
    assert test_words_stats('words.txt') == alpha_list
    assert test_words_stats('wordswithcaps.txt') == alpha_list
    assert test_words_stats('wordswithpunct.txt') == alpha_list
    assert test_words_stats('wordswithnewlines.txt') == alpha_list   

def run_tests():
    # Check file to list of words by printing
    # all_test_file_to_words()

    # Test cleaning of words
    all_test_clean_words()

    # Test resetting of counters
    all_test_reset()

    # Test incrementing of counters
    all_test_add()

    # Test counting of words in a file
    all_test_count_file()

    # Test counting of words in multiple files
    all_test_count_mult_files()

    # Test that total word count is returned correctly
    all_test_word_count_total()

    # Test that unique word count is returned correctly
    all_test_word_count_unique()

    # Test that words are returned alphabetically in a list
    all_test_alpha_words()

    # Test that words are returned as a list of tuples (freq, words)
    all_test_ranked_words()

    # Test that words are returned as a list of tuples (%, words)
    all_test_perc_words()

    # Test that words are returned as a list of tuples (count, %, words)
    all_test_words_stats()

run_tests()
