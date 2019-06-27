# #list comprehension - describing a list in a single pythonic line
# #List comprehension is an elegant way to define and create list in Python.
# #These lists have often the qualities of sets, but are not in all cases sets. 
# #List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce().
# #1.
# squares = []
# for x in range(10):                       #Using For loop
#     squares.append(x**2)
# print(squares)   
# # # ( OR )
# squares = [x**2 for x in range(10)]       #Using Lists Comprehension
# print(squares)


# #2.Using Loops
# pairs = []
# for x in [9,8,7]:                           #Using For loop
#     for y in [7,2,9]:
#         if x != y:
#             pairs.append((x, y))
# print(pairs)
# #( OR )
# pairs = [(x,y) for x in [9,8,7] for y in [7,2,9] if x!=y]   #Using Lists Comprehension
# print(pairs)

# #3.Evenlist
# evenList = [x for x in range(0,11) if x%2==0]
# print(evenList)
