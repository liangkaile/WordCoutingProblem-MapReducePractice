#!/usr//bin/env python
from operator import itemgetter
import sys

current_word = None
current_length = 0
word = None
max_count = 0
max_word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    length, word, count = line.split('\t', 2)

    # convert length count (currently a string) to int
    try:
        length = int(length)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if(length>=10 and length<20):
        if current_length ==length:
            current_word = word
            #get the max count word
            if count > max_count:
                max_count=count
                max_word = current_word
        else:
            if max_count:
                #print out the max count word
                print '%s\t%s\t%s' %(current_length,max_word,max_count)
            current_word = word
            max_word = word
            current_length = length
            max_count = count
    else:
        continue

# do not forget to output the last word if needed!
if current_length ==length:
    print '%s\t%s\t%s' %(current_length,max_word,max_count)

