from wordcount import WordCount

def test_file_to_words(file):
    """
    This tests that the file properly opens and returns a list of the words
    without spaces or new lines.
    """
    wc = WordCount()
    return wc._file_reader(file)

def test_clean_words(list):
    wc = WordCount()
    for i in range(len(list)):
        list[i] = wc._word_cleaner(list[i])
    return list

def test_reset(num, list_of_words):
    wc1 = WordCount()
    wc2 = WordCount()

    # increase wc1
    wc1._word_counter += num
    for word in list_of_words:
        wc1._words_seen[word] += 1

    # check that they are now different
    if num > 0:
        assert wc1._word_counter > wc2._word_counter
    if len(list_of_words) > 0:
        assert len(wc1._words_seen.items()) > len(wc2._words_seen.items())

    #reset
    wc1.reset()

    # check that wc1 has indeed reset
    assert wc1._word_counter == wc2._word_counter
    assert wc1._word_counter == 0
    assert len(wc1._words_seen.items()) == len(wc2._words_seen.items())
    assert len(wc1._words_seen.items()) == 0

def test_add(list_of_words):
    wc = WordCount()
    manual_count = 0
    for word in list_of_words:
        wc._add_to_count(word)
        manual_count += 1
        assert wc._words_seen[word] > 0
        assert wc._word_counter == manual_count

def test_count_file(filename):
    wc = WordCount()
    wc.count_file(filename)
    assert wc._word_counter == 10
    assert wc._words_seen['zero'] == 0
    assert wc._words_seen['one'] == 1
    assert wc._words_seen['two'] == 2
    assert wc._words_seen['three'] == 3
    assert wc._words_seen['four'] == 4

def test_count_mult_files(list_of_filenames):
    wc = WordCount()
    mult = 1
    for file in list_of_filenames:
        wc.count_file(file)
        assert wc._word_counter == 10*mult
        assert wc._words_seen['zero'] == 0
        assert wc._words_seen['one'] == 1*mult
        assert wc._words_seen['two'] == 2*mult
        assert wc._words_seen['three'] == 3*mult
        assert wc._words_seen['four'] == 4*mult
        mult += 1

    


def run_tests():
    file_to_words = False
    clean_words = True
    reset = True
    adding_words = True
    count_file = True
    count_mult_files = True

    if file_to_words: 
        print "Testing ability to open file and return words: "
        assert test_file_to_words('blank.txt') == []
        print test_file_to_words('words.txt')
        print test_file_to_words('wordswithcaps.txt')
        print test_file_to_words('wordswithpunct.txt')
        print test_file_to_words('wordswithnewlines.txt')

    if clean_words:
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

    if reset:
        print "Testing proper reset."
        test_reset(1, ['hi'])
        test_reset(4, ['a', 'b', 'c', 'd'])

    if adding_words:
        print "Testing addition of words to increase counts."
        test_add([])
        test_add(['a', 'b', 'c', 'd'])

    if count_file:
        "Testing addition of files to increase counts."
        test_count_file('words.txt')
        test_count_file('wordswithcaps.txt')
        test_count_file('wordswithpunct.txt')
        test_count_file('wordswithnewlines.txt')
    
    if count_mult_files:
        print "Testing addition of multiple files to up counts w/o reset."
        all_files = ['words.txt', 'wordswithcaps.txt', 'wordswithpunct.txt', \
            'wordswithnewlines.txt']
        test_count_mult_files(all_files[:1])
        test_count_mult_files(all_files[:2])
        test_count_mult_files(all_files[:3])
        test_count_mult_files(all_files[:4])
        test_count_mult_files(all_files)

run_tests()
