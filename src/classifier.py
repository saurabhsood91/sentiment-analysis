#!/usr/bin/python
from math import log
from filereader import FileReader

class NaiveBayesClassifier(object):
    def __init__(self, positive_file, negative_file):
        # Parse positive reviews
        self.pos_filereader = FileReader(positive_file, "positive")
        self.positive_words = self.pos_filereader.ParseFile()
        self.positive_word_count = len(self.positive_words)
        self.neg_filereader = FileReader(negative_file, "negative")
        self.negative_words = self.neg_filereader.ParseFile()
        self.negative_word_count = len(self.negative_words)
        self.bag_of_words = self.positive_words + self.negative_words
        # print self.bag_of_words
        # print len(self.positive_words),':' ,self.pos_filereader.GetWordCount()
        # print len(self.negative_words),':' ,self.neg_filereader.GetWordCount()
        self.total_word_type_count = len(self.bag_of_words)
        # print self.total_word_type_count
        # self.positive_words = self.filereader.GenerateCounts()
        # self.positive_word_count = self.filereader.GetWordCount()
        # # Parse negative reviews
        # self.filereader.SetFile(negative_file)
        # self.filereader.SetSentiment("negative")
        # self.filereader.ParseFile()
        # self.negative_words = self.filereader.GenerateCounts()
        # self.negative_word_count = self.filereader.GetWordCount()
        # self.MergeCounts()

        # print self.total_word_type_count
    def Classify(self, test_file):
        # create new filereader
        # don't pass sentiment to the function. It will be set to None
        test_file_reader = FileReader(test_file)
        # Parse the file to read all the reviews
        test_file_reader.ParseFile()
        reviews = test_file_reader.GetReviews()
        # print reviews
        # Iterate over the reviews in the test set
        for id, review in reviews.iteritems():
            # print review
            # split the review into words
            cur_review = review["review"]
            review_words = cur_review.split()
            # print review_words
            # For each word in the review calculate a probability
            # use add-1 smoothing
            positive_probability = 0
            negative_probability = 0
            for word in review_words:
                # if word is in the positive wordlist
                if word in self.positive_words:
                    # print self.bag_of_words[word]
                    positive_probability += log(self.positive_words[word] + 1) - (log(self.total_word_type_count + self.positive_word_count))
                else:
                    # just use the count as 1
                    positive_probability += 0 - log(self.total_word_type_count + self.positive_word_count)
                if word in self.negative_words:
                    negative_probability += log(self.negative_words[word] + 1) - (log(self.total_word_type_count + self.negative_word_count))
                else:
                    negative_probability += 0 - log(self.total_word_type_count + self.negative_word_count)
            # print positive_probability, negative_probability
            if positive_probability > negative_probability:
                print review["id"], ":" ,"Positive"
            else:
                print review["id"], ":" , "Negative"
