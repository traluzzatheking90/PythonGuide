#!/usr/bin/env python3

myList = []

for i in range(10, 30, 1):

    if i % 2 == 0 and i < 25:
        myList.append(i)

print(myList)

## STESSA COSA MA USANDO LA LIST COMPRENSION
secondList = [x for x in range(10, 30) if x % 2 == 0 and x < 25]
print(secondList)
