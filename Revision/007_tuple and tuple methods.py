# empty tuple
# t1 = ()

# tuple with numbers
# t2 = (1,2,3,4,5)

# mixed datatype tuple
# t3 = ('Sanan', 25, True)

# Single Element Tuple, Comma is necessary
# t4 = (2,)
# print(t4)

# Common Tuple Methods

# count - Returns the number of times x appears in the tuple
t1 = (1,2,3,4,51,2,5,11,1,56,7,2,2,11,1)
# print(t1.count(1))

# index - Returns the index of the first occurrence of x .
# print(t1.index(11))

# Tuple Characteristics
# Immutable: Once created, elements cannot be changed.
# Faster than lists: Accessing elements in a tuple is faster than in a list.
# Can be used as dictionary keys: Since tuples are immutable, they can be used as keys in dictionaries

# Accessing Tuple Elements

# t1 = (10,20,30,40,50)

# print(t1[1])
# print(t1[0:])
# print(t1[:3])
# print(t1[3:])
# print(t1[:-1])
# print(t1[:-2])

# Tuple Packing and Unpacking

# packing
# info = ("Sanan", 25, "Data Scientist", True)

# #unpacking
# name, age, profession, is_male = info
# print(name)
# print(age)
# print(profession)
# print(is_male)