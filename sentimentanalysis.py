# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
''' read data and prepare it for reading by the NLP we have in NLTK'''
data = open("input.txt","rt")
text = data.read()

'''create the sentiment analyzer using NLTK's built in VADER analyzer'''
sentimentVader = SentimentIntensityAnalyzer()

'''we will now calculate the sentiment values of this text'''
sentimentDict = sentimentVader.polarity_scores(text)
print("The overall sentiment value of this text is : ")
print(sentimentDict["compound"])
print("this score is on a range of 1 (most positive) and -1 (most negative), and this score indicates the above text is overall: ")
if sentimentDict["compound"] < 0.5:
    print("negative")
else:
    print("positive")


