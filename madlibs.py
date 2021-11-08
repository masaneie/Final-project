import re

pizza = open("pizza.txt", "r")
pizza = pizza.read()

taglist = re.findall(r"\[\[(.*?)\]\]", pizza)

userwords = []

for tag in taglist:
	userword = input("Please enter a " + tag + ": ")
	userwords.append(userword)

word_list = iter(userwords)
output = re.sub(r"\[\[\w+]\]", lambda L: next(word_list), pizza, 0, re.MULTILINE)

print(output)
