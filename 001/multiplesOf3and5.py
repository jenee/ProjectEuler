# http://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples 
#   of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# sum variable is 0
sum = 0

# loop i through 1 to < 1000
for i in range(1000):
# # if  i % 3 is 0 or i % 5 is zero
   if i % 3 == 0 or i % 5 == 0:
# # # add i
      sum += i

# print sum
print sum
