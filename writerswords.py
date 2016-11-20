from wordcount import WordCount
    # values for formatting
RANK_IND = 5
COUNT_IND = 10
PERC_IND = 25
WORD_IND = 25


def writers_words(list_of_files, outputfile):

    counter = WordCount()
    for file in list_of_files:
        counter.count_file(file)
    output = open(outputfile, 'w')

    stats = counter.word_stats()

    output.write("Total words counted: " + repr(counter.word_count_total()) \
        + '\n')
    output.write('Rank'.rjust(RANK_IND) \
                + 'Word'.rjust(WORD_IND) \
                + 'Count'.rjust(COUNT_IND) \
                + ' '*5 \
                + 'Percentage'.ljust(PERC_IND) \
                + '\n')

    rank = 1

    for (count, perc, list_of_words) in stats:
        for word in list_of_words:
            newline = repr(rank).rjust(RANK_IND) \
                + word.rjust(WORD_IND) \
                + repr(count).rjust(COUNT_IND) \
                + ' '*5 \
                + repr(perc).ljust(PERC_IND) \
                + '\n'
            output.write(newline)
        rank += 1

    output.close()

    return True

# uncomment to run on Shakespeare's full works from the Gutenberg project
writers_words(['shakespeare.txt'], 'shakespearestats.txt')
