'''
http://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

maxFactor = 1000
#maxFactor = int(math.sqrt(1000))

foundTriplet = False
product = 0

for c in range(3,maxFactor):
   if foundTriplet:
      break
   for b in range(2,c):
      if foundTriplet:
         break
      for a in range(1,b):
         if a + b + c == 1000:
            aSqrd = a ** 2
            bSqrd = b ** 2
            cSqrd = c ** 2

            if aSqrd + bSqrd == cSqrd  :
               print "a="+str(a)
               print "b="+str(b)
               print "c="+str(c)
               foundTriplet = True
               product = a*b*c
               break


print product
