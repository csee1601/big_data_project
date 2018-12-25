import sys

for line in sys.stdin:
    word_list = line.strip().split(' ')
    for word in word_list:
        print ('\t'.join([word.strip(), str(1)]))
