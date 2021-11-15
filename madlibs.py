import re
import os
import argparse
import sys

from datetime import *

if len(sys.argv) > 1:
    filename = sys.argv[1]
    while os.path.isfile(filename) == False:
        filename = input("File does not exist. Please try again: ")
else:
	filename = input("Please type in the filename with extension (e.g., sample.txt): ")
    
madlib = open(filename)
madlib = madlib.read()

taglist = re.findall(r"\[\[(.+?)\]\]", madlib)

userwords = []

for tag in taglist:
	userword = input("Please enter " + tag + ": ")
	userwords.append(userword)

word_list = iter(userwords)

def takenext(x):
    return next(word_list)

output = re.sub(r"\[\[(.+?)\]\]", takenext, madlib, flags=re.M)
output = re.sub(r'(\ba\b) ([aiueo])', r'an \2', output, flags=re.I|re.M)

timestamp =str(datetime.now())
timestamp = re.sub(r"\W", r"-", timestamp) 

fileout = open(f'{filename[:-4]}_{timestamp[:-7]}.txt', "w")
for line in output:
    fileout.write(line)
fileout.close()

print('Your completed madlib is: ' + output)
print(f'Your madlib is saved in {filename[:-4]}_{timestamp[:-7]}.txt')
