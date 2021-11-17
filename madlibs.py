import re
import os
import sys

from datetime import *

if len(sys.argv) > 1:
    filename = sys.argv[1]
    if os.path.isfile(filename) == False:
        sys.exit("That madlib file does not exist. Please enter the command again.")
else:
    filename = input("Please enter a madlib filename with extension (e.g., sample.txt): ")
    while os.path.isfile(filename) == False:
        filename = input("That madlib file does not exist. Please enter a different filename: ")

madlibs = open(filename)
madlib = madlibs.read()
madlibs.close()

taglist = re.findall(r"\[\[(.+?)\]\]", madlib)

userwords = []

for tag in taglist:
    userword = input("Please enter " + tag + ": ")
    userwords.append(userword)

word_list = iter(userwords)

def takenext(x):
    return next(word_list)

output = re.sub(r"\[\[(.+?)\]\]", takenext, madlib)
output = re.sub(r'(\ba\b) ([aiueo])', r'\1n \2', output, flags=re.I)

timestamp =str(datetime.now())
timestamp = re.sub(r"\W", r"-", timestamp) 

fileout = open(f'{filename[:-4]}_{timestamp[:-7]}.txt', "w")
for line in output:
    fileout.write(line)
fileout.close()

print('Your completed madlib is: ' + output)
print(f'Your madlib is saved in {filename[:-4]}_{timestamp[:-7]}.txt')
