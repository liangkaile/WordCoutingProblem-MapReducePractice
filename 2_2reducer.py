#!/usr/bin/env python
from operator import itemgetter
import sys

word = None
length = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    length, word, count = line.split('\t', 2)

    # convert count and length (currently a string) to int
    # print each line
    try:
        length = int(length)
        count = int(count)
        print '%s\t%s\t%s' %(length,word,count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
