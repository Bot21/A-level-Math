import math

n = int(input("Type in number of trails \n >"))
r = int(input("Type in number of successes \n >"))
p = float(input("Type in the probability of success \n >"))
NR = n - r
q = 1 - p

n_factorial = 1
r_factorial = 1
NR_factorial = 1

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   n_factorial = 1
else:
   for i in range(1,n + 1):
       n_factorial = n_factorial*i


if r < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif r == 0:
   r_factorial = 1
else:
   for i in range(1,r + 1):
       r_factorial = r_factorial*i


if NR < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif NR == 0:
    NR_factorial = 1
else:
   for i in range(1,NR + 1):
       NR_factorial = NR_factorial*i
       
       
ans = (n_factorial)/(r_factorial*NR_factorial) * (p**r) * (q**NR)
 
print(ans)
 
