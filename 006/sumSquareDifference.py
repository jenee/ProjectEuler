'''
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025- 385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

maxNum = 100
listOfNums = range(1,maxNum+1)

sumNums = sum(listOfNums)

print "Sum nums: " +str(sumNums)

sumSquares = 0;
for i in listOfNums:
   sumSquares += i ** 2

print "Sum of all squares: " + str(sumSquares)

squaredSum = sumNums ** 2

print "Square of sum of all nums: " + str( squaredSum)

diff = squaredSum -sumSquares 

print "diff = " + str(diff)
