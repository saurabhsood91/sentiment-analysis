#!/usr/bin/python
from classifier import NaiveBayesClassifier

a = NaiveBayesClassifier("training_data/hotelPosT-train.txt","training_data/hoteNegT-train.txt")
a.Classify("test_data.txt")
