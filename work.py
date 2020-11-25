"""
Live Project Lab 6 
Have used a local text file as the source

"""
import string 
import re
with open("gitWorkflow.txt") as infile, open("gitWorkflow_clean.txt", "w") as outfile:
    for line in infile:
        # make all one case
        # remember to add new string 'lowerline = ' strings are immutable!
        lowerline = line.lower()
         
        # remove punctuation with regular expression
        no_punctuation = re.sub(r'[^\w\s]','', lowerline)
         
        # split into words - whitespace is default separator
        # words is a list of individual words in the line 
        words = no_punctuation.split()
         
        # write all words one word per line
        for word in words:
            outfile.write(word)
            # write will only accept one argument
            outfile.write("\n")
            
