'''
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


# curDivisor = 2
curDivisor = 2

baseNum = 600851475143
# baseNum = 13195

# maxPrimeFactor = 2
maxPrimeFactor = 2

# minMaxPrimeFactor = 600851475143 / 2
minMaxPrimeFactor = baseNum / 2

while curDivisor < minMaxPrimeFactor and baseNum > maxPrimeFactor:
   if baseNum % curDivisor == 0:
      tempBase = baseNum / curDivisor
      #print "curDiv="+str(curDivisor)+", tempBase="+str(tempBase)
      if curDivisor > maxPrimeFactor:
         maxPrimeFactor = curDivisor
      baseNum = tempBase
      curDivisor = 2
   else:
      #print curDivisor
      curDivisor += 1
   
print maxPrimeFactor





