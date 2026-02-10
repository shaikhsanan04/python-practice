# A set in Python is an unordered, mutable, and unique collection of elements. It does not allow duplicate values.

# Creating a Set:

# creating an empty set
# Empty set (must use set(), not {})
# s1 = set()
# print(s1)

# creating a set with elements
# s2 = {1,2,3,4,5} #does not have duplicate values
#s2 = {1,2,3,4,5,2,2,1,5,3,2} #does have duplicate values
# print(s2)

# mixed element set
# s3 = {'Sanan',25,2000,76.10}
# print(type(s3))

# creating a set from list
# l1 = [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5]
# s1 = set(l1)
# print(s1)

# ---------------------------------------------------------------------------
# Common Set Methods


s1 = {1,2,3,4,5}

# add  - adds an element to the set
# s1.add(6)
# print(s1)

# update : add multiple elements form an iterable
# s1.update([6,7,8,9,10])


# remove - removes an element form the set, raises an error if not found
# s1.remove(45) # will raise an error
# s1.remove(4) # will not raise an error and remove the element
# print(s1)

# discard - removes an element form the set, does not raise an error if not found
# s1.discard(45) # will not raise an error
# s1.discard(4) # will not raise an error and remove the element

# pop  - removes and return a random element from the set
# e = s1.pop()
# print(e)

# copy - returns a shallow copy
# s2 = s1.copy()
# print(s2)

# clear - rmeove all the elements from the list
# s1.clear()
# print(s1)


# ---------------------------------------------------------------------

# SET OPERATIONS

s1 = {1,2,3}
s2 = {1,2,3,4,5,6,7,8,9}

# union - Returns a new set with all unique elements from both sets
# s3 = s1.union(s2)
# print(s3)

# intersection - returns a set with elements common in both sets
# s3 = s1.intersection(s2)
# print(s3)

# difference - returns a set with elements in set 1 and not set 2
# s1 = {45,65,89}
# s2 = {10,35,89}
# s3 = s1.difference(s2)
# print(s3)

# symmetric difference - Return a set that contains all items from both sets, except items that are present in both sets

# s1 = {45,65,89}
# s2 = {10,35,89}
# s3 = s1.symmetric_difference(s2)
# print(s3)

# issubset - Returns True if set1 is a subset of set2 
# s1 = {1,2,3}
# s2 = {1,2,3,4,5,6,7,8}
# s2 = {4,5,6,7,8}
# print(s1.issubset(s2))

# issuperset - Returns True if set1 is a superset of set2 .
s1 = {1,2,3,4,5,6}
s2 = {4,5,6}
print(s2.issuperset(s1))
# print(s1.issuperset(s2))
