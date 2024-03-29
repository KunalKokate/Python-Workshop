# #Exception Handling
# try:                   #put that code in it which you think is a error
# except <Exception>:    #put the posssible exception here
# 	print("Some error")
# else
# 	print("All went well")

#ex1-IOError
try:
	fh = open("example_23.txt","w")
	fh.write("This is my test file for exception handling")
except IOError:
	print("It's a File Error")
else:
	print("All went well")

# ex2- KeyError
dict1={"jan":31,"march":30,"april":31}
try:
	print(dict1["march"])
except KeyError: #if you put any other error for example IndexError then it will crash.
	print("Key could be wrong")
else:
	print("All went well")

#ex3 - ValueError
try:
	a = int("dog")
    print(a)
except ValueError:
	print("Value error is there")
else:
	print("Sab thik hai")

#ex4-TypeError
try:
	print("3"+3)
except TypeError:
	print("Its a Type error")
else:
	print("All is well")

#ex4-ZeroDivisionError = raised when division by zero takes place for all numeric types.
try:
	val = 5/0
except ZeroDivisionError:
	print("Its a Zero Division Error")
else:
	print("All is well")

#ex5 - IndexError
try:
	list1 = [1,2,3,4,5]
	print(list1[12])
except IndexError:
	print("Error Caught")
else:
	print("All is welll")