import re

pizza = open("pizza.txt", "r")
pizza = pizza.read()

taglist = re.findall(r"\[\[(.+?)\]\]", pizza)

userwords = []

for tag in taglist:
	userword = input("Please enter a " + tag + ": ")
	userwords.append(userword)

word_list = iter(userwords)

def takenext(x):
    return next(word_list)

testpizza = re.sub(r"\[\[.+?\]\]", takenext, testpizza, 0, re.MULTILINE)

print(testpizza)
