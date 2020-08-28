# HackerRank - Maximize it! 

import itertools

k, m = map(int, input().strip().split(' '))

lst = list()

for i in range(k):
    lst.append(input().split(' ')[1:])

smax = 0
for j in itertools.product(*lst):
    modulo = sum([int(x)**2 for x in j]) % m
    if modulo > smax:
        smax = modulo

print(smax)
