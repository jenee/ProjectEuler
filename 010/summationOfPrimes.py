'''
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def isPrime(num):
   numIsPrime = True
   for i in range(2,num):
      if num % i == 0:
         return False
   return numIsPrime


maxNum = 2000000
allPossiblePrimes = range(2,maxNum)

sumOfPrimes = 0

for possiblePrime in allPossiblePrimes:
   if isPrime(possiblePrime):
      sumOfPrimes += possiblePrime
      print possiblePrime
      for multiple in allPossiblePrimes[possiblePrime::possiblePrime]:
         allPossiblePrimes.remove(multiple)
      print len(allPossiblePrimes)
print sumOfPrimes

#too slow. Might want to look into a combinatorics solution?
