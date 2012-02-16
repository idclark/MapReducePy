import sys
from operator import itemgetter

current_word = None
current_count = 0
word = None

for line in sys.stdin:

    line = line.strip()
    #remove white space

    word, count = line.split('\t', 1)
    #parse input from map.py

    try:
        count = int(count)
        #convert count from string to int
    except ValueError:
        countinue
        # count was not a number so ignore this line

    if current_word == word:
        current_count += count

    else:
        if current_word:
            print current_word, current_count
            #write result to STDOUT

        current_count = count
        current_word = word

if current_word == word:
    print current_word, current_count
#don't foreget to output last word if needed

