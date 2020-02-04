#!/usr/bin/python3
# - * - encode: utf-8 - * -

import sys, re

input_file = sys.argv[1]
word_to_search = sys.argv[2]

with open(input_file, 'r') as f:
	lines = f.readlines()
	f.close()

for line in lines:
    array = re.findall(word_to_search, line)
    if  word_to_search in array:
         words = line.split()
         for word in words:
             if word not in array:
                 print(word, end=' ')
             else:
                 print('\033[91m' + word + '\033[0m')
         print('')
