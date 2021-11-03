import re

pizza = open("pizza.txt", "r")
pizza = pizza.read()

taglist = re.findall(r"\[\[\w+]\]", pizza)
