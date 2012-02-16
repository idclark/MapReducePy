import sys

#input from standard input 
for line in sys.stdin:

    line = line.strip()
    #remove white space
    
    words = line.split()
    #split line into individual words
    
    for word in words:
    #output here will become input for the reducer
    #tab demiminated; min word count is 1
        
        print word, 1