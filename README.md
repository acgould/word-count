# word-count

This repository contains a number of files pertient to counting and ranking words in text files.

## wordcount.py

This file implements the WordsCount class. This class allows you to count the total number of words, the total occurences of each of those words, and return a full list of the words seen, sorted alphabetically and by popularity. You may also return the absolute count, the percentage of total words, or both.

All words are stored in lowercase. Trailing and leading apostrophes, as used for plural posessives and certain contractions, will be chopped off. 

The counting system uses an int counter for the total count and a defaultdict(int) for each word's individual count. This avoids the step of first checking if the word is already in the dictionary before incrementing the counter.

The counter does not automatically reset between files so that you might input multiple files by the same author in the same counter.

reset() allows for a manual reset of the counter. 

Words are read in from the files and split by whitespace. They are then 'cleaned' by becoming entirely lowercase alphabetic characters and removing trailing and leading punctuation using str.lstrip() and str.rstrip() with the following set of non-alpha chars:
"',.!?<>()[]:;-_*&#$%@^

count_file(filename) takes in a string filename. The corresponding file is opened, and its words are added to the counter.

word_count_total() returns the total number of words which have been counted.

word_count_unique() returns the number of unique words which have been counted.

word_count(word) takes in a string word and returns the current count for that word, which may be 0.

words_alphabetical() returns a list of all words, sorted alphabetically.

To return the rankings, the dictionary of word counts is converted to a defaultdict(list) where the keys are the counts and the values are lists of words with those counts.

words_ranked() returns a list of tuples, where each tuple is (frequency, [list of words with that frequency]).

words_percent() returns a list of tuples, where each tuple contains (frequency percentage of total words, [list of words]).

To get both the absolute frequency (count) and the relative frequency (percentage), use word_stats(). This function returns a list of tuples, where each tuple contains (count, percentage, [list of words]).

## test.py
This file implements a series of tests to check the functionality of WordCount. It relies on the following text files:
* blank.txt
* words.txt
* wordswithcaps.txt
* wordswithpunc.txt
* wordswithnewlines.txt
* wordswithdupfreqs.txt

## Shakespeare 
The complete works of Shakespeare found in shakespeare.txt originated from the Gutenberg Project: 
https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

To see the output of writerswords for the Shakespeare texts, see shakespearestats.txt.