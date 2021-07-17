#Count the number of unique paths to travel from the top left to the bottom right of a lattice of size n*n.

import math
n=int(input())
result=(math.factorial(2*n))/(math.factorial(n)*math.factorial(n))
print(result)
