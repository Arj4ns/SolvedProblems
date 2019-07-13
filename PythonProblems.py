# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:16:20 2019

@author: Arjan
"""
from functools import reduce
import math

def evenFibArray():
    fibonacci = [0, 1]
    evenFibonacci = [0]
    result = 0
    i = 0
    while result <= 4000000:
        result = fibonacci[i] + fibonacci[i + 1]
        if result % 2 == 0:
            evenFibonacci.append(result)
        fibonacci.append(result)
        i = i + 1
    return evenFibonacci


#I did not come up with this algorithm. But it's the best one I've seen for factoring in python
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def checkPrime(a):
    newArray = []
    for i in range(0, len(a)):
        prime = True
        for j in range(2, a[i]):
            if a[i] % j == 0:
                prime = False
                break
        if prime == True:
            newArray.append(a[i])
    return newArray

def numberPalindromes():
    finalArray = []
    for i in range(1, 999):
        for j in range(1, 999):
            result = i * j
            listResult = list(map(int, str(result)))
            midpoint = len(listResult)//2
            first = listResult[:midpoint]
            second = listResult[midpoint:]
            revSecond = second[::-1]
            #print(str(first) + " and " + str(second))
            if first == revSecond:
                finalArray.append(result)
    finalArray.sort()
    return finalArray
            
def evenlyDivisable():
    found = False
    count = 20
    while found == False:
        if count % 1 == 0 and count % 2 == 0 and count % 3 == 0 and count % 4 == 0 and count % 5 == 0 and count % 6 == 0 and count % 7 == 0 and count % 8 == 0 and count % 9 == 0 and count % 10 == 0 and count % 11 == 0 and count % 12 == 0 and count % 13 == 0 and count % 14 == 0 and count % 15 == 0 and count % 16 == 0 and count % 17 == 0 and count % 18 == 0 and count % 19 == 0 and count % 20 == 0:
            found = True
        count = count + 1
    return count - 1

def sumOfTheSquares(n):
    tempList = []
    for i in range(1, n + 1):
        square = i ** 2
        tempList.append(square)
    finalResult = sum(tempList)
    return finalResult

def squareOfTheSums(n):
    finalResult = 0
    for i in range(1, n + 1):
        finalResult = finalResult + i
    return finalResult ** 2

def findPrimes(a):
    newArray = []
    for i in range(0, len(a)):
        prime = True
        for j in range(2, a[i]):
            if a[i] % j == 0:
                prime = False
                break
        if prime == True:
            newArray.append(a[i])
    return newArray

def sieveOfEratosthenes(limit):
    numbers = [True] * (limit + 1)
    p = 2
    primes = []
    while p * p <= limit:
        if numbers[p] == True:
            for i in range(p * p, limit + 1, p):
                numbers[i] = False
        p = p + 1
        
    for i in range(2, len(numbers)):
        if numbers[i] == True:
            primes.append(i)
    return primes

print(sieveOfEratosthenes(104750))
        
    
    
    