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
                print self.bag_of_words
