# Jessie Chapman
# Lab 2 - word_count.py: Prints out all the unique words,
# their frequencies, and the total number of words (including
# the multiples of unique words) in a given input file. Also
# alphabetizes the list of words.
# Date: 2/20/2014

import sys

def count_words(f):
        words = []
        #go through file and add each word to the list                          
        for line in f:
                for word in line.split():
                        word.lower()
                        words.append(word)

        #alphabetize the words                                                  
        words.sort()

        #get rid of multiples of words                                          
        #and alphabetize it                                                     
        temp = set(words)
        ordered = list(temp)
        ordered.sort()

        count = []
        num = 0
        #get the frequency of each word in the file                             
        for i in range(len(ordered)):
                for j in range(len(words)):
                        if ordered[i] == words[j]:
                                num = num + 1
                count.append(num)
                num = 0

        #print the words, how many times it occured                             
        for i in range(len(ordered)):
                print ordered[i], count[i]

        print "Total number of words:", len(words)
                          
if __name__ == '__main__':
        f = sys.argv[-1]
	try:
                f = open(f, 'r')
		count_words(f)
        except (OSError, IOError) as e:
                print "Invalid file"
