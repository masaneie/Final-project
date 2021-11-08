import re

pizza = open("pizza.txt", "r")
pizza = pizza.read()

taglist = re.findall(r"\[\[(.+?)\]\]", pizza)

userwords = []

for tag in taglist:
	userword = input("Please enter " + tag + ": ")
	userwords.append(userword)

word_list = iter(userwords)

def takenext(x):
    return next(word_list)

output = re.sub(r"\[\[(.+?)\]\]", takenext, pizza, 0, re.MULTILINE)

print(output)
