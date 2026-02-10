# A list in Python is an ordered, mutable collection of elements. It can contain elements of different types.


# list1 = []  empty list

# list2 = [1,2,3,4,5]
# print(list2)

# list3 = ["Sanan", 25, True]
# print(list3)

# l1 = [1,2,3,4,5,6,7,8,9]
# l1[0] = 22
# print(l1)
# ------------------------------------------------------------

# Common List Methods

l1 = [1,2,3,4,5,6,7,8,9]

# append : adds an element at the end of the list
# l1.append(10)
# print(l1)

# extend : extends the list by passing another list
# l2 = [10,11,12]
# l1.extend(l2)
# print(l1)

# insert : it inserts an element at the given index
# l1.insert(4,5656)
# print(l1)

# remove : Removes the first occurrence of x in the list
# l1.remove(9)
# print(l1)

# pop : removes and returns the element at index (returns last element if no index is passed)
# l1.pop(3) # index passed
# l1.pop() # no index passed
# print(l1)

# index : returns the index of the first occurence
# print(l1.index(3))

# count : returns the no. of times an element occurs in the list
# print(l1.count(3))

# sort : sorts the list in ascending order
# print(l1.sort())

# reverse : reverses the list
# print(l1.reverse())

# copy : returns a shallow copy of the list
# l3 = l1[0:3].copy()
# print(l3)
# print(l1)
# print("----------------------------------")
# l3.extend([45,56,78,89,458])

# print(l3)
# print(l1)

# clear : clears the list ie remove all the elements form the list
# l1.clear()
# print(l1)