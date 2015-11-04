#! /usr/bin/python
# This module parses the file and creates a dict of all reviews

class FileReader(object):
    def __init__(self, filename, sentiment=None):
        # set the initial filename
        self.filename = filename
        # Set the sentiment
        self.sentiment = sentiment

    def SetFile(self, filename):
        # To set the filename
        self.filename = filename

    def SetSentiment(self, sentiment):
        # Set the sentiment
        self.sentiment = sentiment

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
        # Parse the file and create the dict
        self.reviews = {}
        if self.filename != None:
            with open(self.filename, "rb") as training_file:
                for line in training_file:
                    # Get ID
                    split_array = line.split()
                    id = split_array[0]
                    # print id
                    review = "".join(split_array[1:])
                    # print review
                    review = self.RemovePunctuation(review)
                    self.reviews[id] = {
                    "review": review,
                    "sentiment": self.sentiment
                    }
                    # print self.reviews[id]
            return self.reviews
