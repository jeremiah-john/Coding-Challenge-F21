# ACM Research Coding Challenge (Fall 2021)

The solution is in "sentimentanalysis.py", as in the pythons script, not the Jupyter Notebook, although you may also run the program using that file
I utilized the Natural Language Toolkit (NLTK) in this program.

the steps for analyzing the text in my program are simple. I first had to read in the data from the input text file, then convert it to a string object
I then had to set up the NLTK's built in VADER Sentiment Analyzer. I then used the polarity_scores() function of this analyzer to determine the overall score of 
the text.
I tried using PANDAS as well, and you can see this in the commit history of this project, and I also considered splitting up the text from the input into sentences, but seeing as
the VADER analyzer could analyze the whole text on it's own and didn't need to be fed the text line by line, I removed PANDAS and the code I implemented that would have split up the
text into a list of sentences to then be put into a PANDAS dataframe