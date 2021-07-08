import math
from fractions import Fraction

a = float(input("Enter the first term \n >"))
r = float(input("Enter the r factor \n >"))
n = int(input("Enter the nth term \n >"))

number_list = []
term = 0

if n <= 0:
    print("Please enter an integer greater than zero")
else:
    for i in range(1, n + 1):
        term = a*(r**(i-1))
        number_list.append(term)

print(number_list)
print("The sum of all", n, "terms is", sum(number_list))