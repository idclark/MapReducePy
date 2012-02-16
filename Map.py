import sys

def read_input(file):
    for line in file:

        yield line.split()
        # we split the line into words

def main(seperator = '\t'):

    data = read_input(sys.stdin)
    for words in data:

        for word in words:
            print '%s%s%d' % (word, seperator, 1)

        #write results to STDOUT
        #output here will be input for reduce.py
        #tab-deliminated , min word count is 1
if __name__ == "__main()__":
    main()
