import itertools

A = [*set(int(l) for l in input().split())]
B = [*set(int(l) for l in input().split())]
product  = list(itertools.product(A,B))
print(" ".join(map(str,product)),end=" ")