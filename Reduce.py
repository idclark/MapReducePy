import sys
from operator import itemgetter
from itertools import groupby

def read_map_output(file, seperator ='\t'):
    for line in file:
        yield line.rstrip().split(seperator, 1)

def main(seperator = '\t'):
    #input comes form stdin

    data = read_map_output(sys.stdin, seperator = seperator)

    #groupby groups multiple word-count pairs by word,
    #and creates an interator that returns consecutive keys and their group:
        # current_word - string containing a word (the key)
        # group - interator yielding all ["<current_word>", "<count>"] items

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, seperator, total_count)

        except ValueError:
                #count was not a number, silently discard
            pass
if __name__ == "__main()":
    main()

