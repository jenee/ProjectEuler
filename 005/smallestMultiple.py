'''
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def isDivisibleByAll20(num):
   retVal = True
   for i in xrange(1,21):
      if (num % i) != 0:
         retVal = False
   return retVal




maxMultiple = 20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1

curVal = maxMultiple
minBound = 20*19*17*13*11*7*5*3*2

minMult = maxMultiple

while curVal > minBound:
   if isDivisibleByAll20(curVal):
      if curVal < minMult:
         minMult = curVal
         print minMult
   curVal -= 1

print minMult
