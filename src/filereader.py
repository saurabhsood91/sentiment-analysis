#! /usr/bin/python
# This module parses the file and creates a dict of all reviews

class FileReader(object):
    def __init__(self, filename, sentiment=None):
        # set the initial filename
        self.filename = filename
        # Set the sentiment
        self.sentiment = sentiment

        # Initialize empty dicts
        self.reviews = {}

    def SetFile(self, filename):
        # To set the filename
        self.filename = filename

    def SetSentiment(self, sentiment):
        # Set the sentiment
        self.sentiment = sentiment

    def GetWordCount(self):
        return self.word_count

    def RemovePunctuation(self, str):
        # Remove commas, full stops, semicolons, /, hyphens
        str = str.replace(",", "")
        str = str.replace(".", "")
        str = str.replace(";", "")
        str = str.replace(";", "")
        str = str.replace("/", "")
        str = str.replace("-", "")
        return str

    def ParseFile(self):
        self.reviews = {}
        # Parse the file and create the dict
        if self.filename != None:
            with open(self.filename, "rb") as training_file:
                for line in training_file:
                    # Get ID
                    split_array = line.split()
                    id = split_array[0]
                    # print id
                    review = " ".join(split_array[1:])
                    # print review
                    review = self.RemovePunctuation(review)
                    self.reviews[id] = {
                    "review": review,
                    "sentiment": self.sentiment
                    }
                    # print self.reviews[id]
            return self.reviews

    def GenerateCounts(self):
        self.bag_of_words = {}
        self.word_count = 0
        # Generate counts
        for id, review_object in self.reviews.iteritems():
            # split the review into words
            # print review_object
            review = review_object["review"]
            # print review
            review_words = review.split()
            # generate a set of words
            review_words_set = set(review_words)
            # for each word in the set generate counts for the word
            for word in review_words_set:
                # count word in review
                count = review_words.count(word)
                self.word_count += count
                # if the word is in the bag of words, update count
                if word in self.bag_of_words:
                    self.bag_of_words[word] += count
                else:
                    self.bag_of_words[word] = count
        # print self.bag_of_words
        # print self.word_count
        return self.bag_of_words

# if __name__ == "__main__":
#     a = FileReader("training_data/hotelPosT-train.txt", "positive")
#     a.ParseFile()
#     print a.GenerateCounts()
    # a.SetFile("training_data/hoteNegT-train.txt")
    # a.SetSentiment("negative")
    # a.ParseFile()
    # print a.GenerateCounts()
