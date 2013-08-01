'''
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.


'''

def isPalindrome(numNum):
   theNum = str(numNum)
   reversedNum = theNum[::-1]
   if str(theNum) == reversedNum:
      print str(reversedNum)+" == "+str(theNum)
   return (str(theNum) == reversedNum)

maxPal = 0;

#for i 999 to 100
for i in xrange(100,999):
# # for j 999 to 100
   for j in xrange(100,999):
# # # tempProduct = i * j
      tempProduct = i * j
# # # if isPalindrom(tempProduct):
      if isPalindrome(tempProduct):
# # # # if tempProduct > maxPal
         if tempProduct > maxPal:
# # # # # maxPal = tempProduct
            maxPal = tempProduct


print maxPal



