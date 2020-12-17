from scanner import *
from symbol_table import *

file = "test_input.txt"
with open(file, 'r') as file:
    source = file.read()

scan1 = Scanner(source)
scan1.scan()
tokens = scan1.tokens
symbol1 = Symbol_table(tokens)
symbol1.make_table()
symbol_table = symbol1.symbol_table

for i in tokens:
    print(i)
print()
print("============================== Symbol Table ==============================")
print('{0:15s} {1:20s} {2:30s} {3:5s}'.format("Symbol name", "type", "scope", "size"))
print("--------------------------------------------------------------------------")
for j in symbol_table:
    print('{0:15s} {1:20s} {2:30s} {3:5d}'.format(j[0], j[1], j[2], j[3]))
file.close()
