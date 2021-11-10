import re

filename = input("Please type the filename with an extension: ")

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

output = re.sub(r"\[\[(.+?)\]\]", takenext, madlib, 0, re.MULTILINE)
output = re.sub(r'(a) ([aiueo])', r'an \2', output, flags=re.I|re.M)

from datetime import *

timestamp =str(datetime.now())
timestamp = re.sub(r"\W", r"-", timestamp) 

fileout = open(f'{filename[:-4]}_{timestamp[:-7]}.txt', "w")
for line in output:
    fileout.write(line)
fileout.close()

print(f'Your madlib is saved in {filename[:-4]}_{timestamp[:-7]}.txt')
