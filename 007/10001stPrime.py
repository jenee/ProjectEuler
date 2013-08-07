'''
http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def isPrime(num):
   numIsPrime = True
   for i in range(2,num):
      if num % i == 0:
         return False
   return numIsPrime

count = 1
targetNumPrime = 10001
num = 3
lastPrime = 0

while count < 10001:
   if isPrime(num):
      count += 1
      lastPrime = num
   num += 2

print lastPrime
