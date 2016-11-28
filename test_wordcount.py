
# file to test wordcount class in wordcount.py

from wordcount import WordCount

def list_of_strings(length):
    """This function creates a list of strings to aid testing,"""
    list = range(length)
    for i in range(length):
        list[i] = str(i)
    return list

def file_to_words(file):
    """
    This tests that the file properly opens and returns a list of the words
    without spaces or new lines.
    """
    wc = WordCount()
    return wc._file_reader(file)

# def test_file_to_words():
#     print "Testing ability to open file and return words: "
#     assert file_to_words('blank.txt') == []
#     print file_to_words('words.txt')
#     print file_to_words('wordswithcaps.txt')
#     print file_to_words('wordswithpunct.txt')
#     print file_to_words('wordswithnewlines.txt')
#     print file_to_words('wordswithdupfreqs.txt')

def clean_words(list):
    wc = WordCount()
    for i in range(len(list)):
        list[i] = wc._word_cleaner(list[i])
    return list

def test_clean_words():
    print "Testing ability to clean words."
    clean_list = ['a', 'b', 'c', 'd']
    assert clean_words([]) == []
    assert clean_words(['a', 'b', 'c', 'd']) == clean_list
    assert clean_words(['A', 'B', 'C', 'D']) == clean_list
    assert clean_words(['a.', 'b,', 'c?', 'd!']) == clean_list
    assert clean_words(['"a', 'b"', '"(c', 'd!"']) == clean_list
    assert clean_words(['$%^^&*a', '!!!b!!!', 'c)))', 'd-']) \
            == clean_list
    assert clean_words(['Hello!']) == ['hello']
    assert clean_words(["Don't!!"]) == ["don't"]

def proper_reset(num, list_of_words):
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

def test_reset():
    print "Testing proper reset."
    proper_reset(1, ['hi'])
    proper_reset(4, ['a', 'b', 'c', 'd'])
    proper_reset(500, list_of_strings(1000))

def adding_words(list_of_words):
    wc = WordCount()
    manual_count = 0
    for word in list_of_words:
        wc._add_to_count(word)
        manual_count += 1
        assert wc._word_counts[word] > 0
        assert wc._total_words == manual_count

def test_add():
    print "Testing addition of words to increase counts."
    adding_words([])
    adding_words(['a', 'b', 'c', 'd'])
    adding_words(list_of_strings(100))
    adding_words(list_of_strings(100) + list_of_strings(200))

def count_file(filename):
    """ This test only works for my numeric-based test files. """
    wc = WordCount()
    wc.count_file(filename)
    assert wc._total_words == 10
    assert wc._word_counts['zero'] == 0
    assert wc._word_counts['one'] == 1
    assert wc._word_counts['two'] == 2
    assert wc._word_counts['three'] == 3
    assert wc._word_counts['four'] == 4

def test_count_file():
    print "Testing addition of files to increase counts."
    count_file('words.txt')
    count_file('wordswithcaps.txt')
    count_file('wordswithpunct.txt')
    count_file('wordswithnewlines.txt')   

def count_mult_files(list_of_filenames):
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

def test_count_mult_files():
    print "Testing addition of multiple files to up counts w/o reset."
    all_files = ['words.txt', 'wordswithcaps.txt', 'wordswithpunct.txt', \
        'wordswithnewlines.txt']
    count_mult_files(all_files[:1])
    count_mult_files(all_files[:2])
    count_mult_files(all_files[:3])
    count_mult_files(all_files[:4])
    count_mult_files(all_files)    

def total_word_count(list_of_words):
    wc = WordCount()
    manual_count = 0
    for word in list_of_words:
        wc._add_to_count(word)
        manual_count += 1
        assert wc.word_count_total() == manual_count
        assert wc.word_count_total() == wc._total_words

def test_total_word_count():
    print "Testing proper return of total word count."
    total_word_count([])
    total_word_count(list_of_strings(100))
    total_word_count(list_of_strings(1000))
    total_word_count(list_of_strings(1000) + list_of_strings(1000))

def unique_word_count(list_of_words):
    wc = WordCount()
    for word in list_of_words:
        wc._add_to_count(word)
    return wc.word_count_unique()

def test_unique_word_count():
    print "Testing proper return of unique words count."
    assert unique_word_count([]) == 0
    assert unique_word_count(list_of_strings(100)) == 100
    assert unique_word_count(list_of_strings(1000)) == 1000
    assert unique_word_count(list_of_strings(1000) \
        + list_of_strings(1000)) == 1000
    assert unique_word_count(list_of_strings(100) + list_of_strings(50) \
        + list_of_strings(25)) == 100

def alpha_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_alphabetical()


def test_alpha_words():
    print "Testing proper return of all words alphabetically."
    alpha_list = ['four', 'one', 'three', 'two']
    assert alpha_words('blank.txt') == []
    assert alpha_words('words.txt') == alpha_list
    assert alpha_words('wordswithcaps.txt') == alpha_list
    assert alpha_words('wordswithpunct.txt') == alpha_list
    assert alpha_words('wordswithnewlines.txt') == alpha_list
    alpha_num_list = ['1', '2', '3', '4', 'cuatro', 'dos', 'four', 'one', \
        'three', 'tres', 'two', 'uno']
    assert alpha_words('wordswithdupfreqs.txt') == alpha_num_list

def ranked_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_ranked()

def test_ranked_words():
    print "Testing proper return of all words and frequencies ranked."
    alpha_list = [(4, ['four']), (3, ['three']), (2, ['two']), (1, ['one'])]
    assert ranked_words('blank.txt') == []
    assert ranked_words('words.txt') == alpha_list
    assert ranked_words('wordswithcaps.txt') == alpha_list
    assert ranked_words('wordswithpunct.txt') == alpha_list
    assert ranked_words('wordswithnewlines.txt') == alpha_list   
    alpha_num_list = [(4, ['4', 'cuatro', 'four']), \
        (3, ['3', 'three', 'tres']), (2, ['2', 'dos', 'two']), \
        (1, ['1', 'one', 'uno'])]
    assert ranked_words('wordswithdupfreqs.txt') == alpha_num_list

def perc_words(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.words_percent()

def all_test_perc_words():
    print "Testing proper return of all words and frequencies ranked."
    alpha_list = [(0.4, ['four']), (0.3, ['three']), (0.2, ['two']), \
        (0.1, ['one'])]
    assert perc_words('blank.txt') == []
    assert perc_words('words.txt') == alpha_list
    assert perc_words('wordswithcaps.txt') == alpha_list
    assert perc_words('wordswithpunct.txt') == alpha_list
    assert perc_words('wordswithnewlines.txt') == alpha_list   
    alpha_num_list = [(4.0/30, ['4', 'cuatro', 'four']), \
        (3.0/30, ['3', 'three', 'tres']), (2.0/30, ['2', 'dos', 'two']), \
        (1.0/30, ['1', 'one', 'uno'])]
    assert perc_words('wordswithdupfreqs.txt') == alpha_num_list

def words_stats(filename):
    wc = WordCount()
    wc.count_file(filename)
    return wc.word_stats()

def test_words_stats():
    print "Testing proper return of words, counts, and percentages, ranked."
    alpha_list = [(4, 0.4, ['four']), (3, 0.3, ['three']), \
        (2, 0.2, ['two']), (1, 0.1, ['one'])]
    assert words_stats('blank.txt') == []
    assert words_stats('words.txt') == alpha_list
    assert words_stats('wordswithcaps.txt') == alpha_list
    assert words_stats('wordswithpunct.txt') == alpha_list
    assert words_stats('wordswithnewlines.txt') == alpha_list   
