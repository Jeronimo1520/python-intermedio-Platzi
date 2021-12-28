from functools import reduce
#Map function

my_list = [1,2,3,4,5]
squares = [i**2 for i in my_list]
print(squares)

cuadrados = list(map(lambda x: x**2, my_list))
print(cuadrados)

#Filter function

my_list2 = [1,4,5,6,9,13,19,21]

odd = list(filter(lambda x: x % 2 != 0, my_list2))
print(odd)

#Reduce function

myList3 = [2, 2, 2, 2, 2]
    
allMultiplied = reduce(lambda a, b: a * b, myList3)
print(allMultiplied)