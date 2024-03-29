# #Anonymous Functions# #

# #Lambda - works per element
# # lambda is used to create an anonymous function (function with no name). 
# # It is an inline function that does not contain a return statement.
# # It consists of an expression that is evaluated and returned.
# #1:
# sumVal = lambda x,y : x+y
# print(sumVal(3,4))
# print(type(sumVal))

# #2:
# square = lambda x : x**2
# print(square(4))

# #3:
# a = input("Give a 3 digit Number : ")
# sumCal = lambda x : int(x[0])*int(x[1])*int(x[2])
# result = sumCal(a)
# print(result)


#Map(action,collection) - works on many elements
#1.
squareVal=list(map(lambda x: x**2 , [1,2,3,4,5] ))
print(squareVal)

#2.	
square=list(map(lambda x: x**2 , range(10) ))
print(square)