#!/usr/bin/python
from filereader import FileReader

class NaiveBayesClassifier(object):
    def __init__(self, positive_file, negative_file):
        # Parse positive reviews
        self.filereader = FileReader(positive_file, "positive")
        self.filereader.ParseFile()
        self.positive_words = self.filereader.GenerateCounts()
        # Parse negative reviews
        self.filereader.SetFile(negative_file)
        self.filereader.SetSentiment("negative")
        self.filereader.ParseFile()
        self.negative_words = self.filereader.GenerateCounts()
        self.MergeCounts()

        # Compute word count of positive words
        self.positive_word_count = 0
        self.negative_word_count = 0
        for word, count in self.positive_words.iteritems():
            self.positive_word_count += count
        for word, count in self.negative_words.iteritems():
            self.negative_word_count += count
        # print self.positive_word_count
        # print self.negative_word_count

    def MergeCounts(self):
        # set bag of words to initially be positive words
        self.bag_of_words = self.positive_words
        # iterate over the negative reviews dict
        for word,count in self.negative_words.iteritems():
            if word in self.bag_of_words:
                # Add the count to existing count
                self.bag_of_words[word] += count
            else:
                # Add the word to the bag of words
                self.bag_of_words[word] = count
                # print self.bag_of_words
        # Compute the total number of word types
        self.total_word_type_count = len(self.bag_of_words.keys())
        # print self.total_word_type_count
    def Classify(self, test_file):
        # create new filereader
        # don't pass sentiment to the function. It will be set to None
        test_file_reader = FileReader(test_file)
        # Parse the file to read all the reviews
        reviews = test_file_reader.ParseFile()

        # Iterate over the reviews in the test set
        for review in reviews.iteritems():
            # print review
            # split the review into words
            pass
