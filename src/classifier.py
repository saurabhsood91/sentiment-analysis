#!/usr/bin/python
from math import log
from filereader import FileReader

class NaiveBayesClassifier(object):
    def __init__(self, positive_file, negative_file):
        # Parse positive reviews
        self.filereader = FileReader(positive_file, "positive")
        self.filereader.ParseFile()
        self.positive_words = self.filereader.GenerateCounts()
        self.positive_word_count = self.filereader.GetWordCount()
        # Parse negative reviews
        self.filereader.SetFile(negative_file)
        self.filereader.SetSentiment("negative")
        self.filereader.ParseFile()
        self.negative_words = self.filereader.GenerateCounts()
        self.negative_word_count = self.filereader.GetWordCount()
        self.MergeCounts()

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
        for id, review in reviews.iteritems():
            # print review
            # split the review into words
            review_words = review["review"].split()
            # print review_words
            # For each word in the review calculate a probability
            # use add-1 smoothing
            positive_probability = 0
            negative_probability = 0
            for word in review_words:
                # if word is in the positive wordlist
                if word in self.positive_words:
                    # print self.bag_of_words[word]
                    positive_probability += log(self.bag_of_words[word] + 1) - (log(self.total_word_type_count + self.positive_word_count))
                else:
                    # just use the count as 1
                    positive_probability += 0 - log(self.total_word_type_count + self.positive_word_count)
                if word in self.negative_words:
                    negative_probability += log(self.bag_of_words[word] + 1) - (log(self.total_word_type_count + self.negative_word_count))
                else:
                    negative_probability += 0 - log(self.total_word_type_count + self.negative_word_count)

            if positive_probability > negative_probability:
                print "Positive"
            else:
                print "Negative"
