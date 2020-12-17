from scanner import *

file = "test_input.txt"
with open(file, 'r') as file:
    source = file.read()

scan1 = Scanner(source)
scan1.scan()
tokens = scan1.tokens

for i in tokens:
    print(i)

file.close()
