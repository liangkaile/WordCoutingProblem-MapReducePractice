#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
current_length = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    #filter the word has length [10, 20)
    length = len(word)
    if(length>=10 and length<20):
        if current_word == word:
            current_count += count
        else:
            if current_word:
                current_length = len(current_word)
                print '%s\t%s\t%s' %(len(current_word),current_word,current_count)
            current_count = count
            current_word = word
    else:
        continue


#print the last
current_length = len(current_word)
print '%s\t%s\t%s' %(len(current_word),current_word,current_count)

