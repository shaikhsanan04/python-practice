# Creating a list of squares
# squares = [i**2 for i in range (1,11)]
# print(squares)


# using if with list comprehensions
# filtering out even numbers
# even = [i for i in range(1,101) if i%2==0]
# print(even)

# using if-else with list comprehensions
# Replacing even numbers with “Even” and odd numbers with “Odd”even = [i for i in range(1,101) if i%2==0]
# numbers = ["Even" if i%2 ==0 else "Odd" for i in range(1,101)]
# print(numbers)

# Nested Loops in List Comprehension
# pairs = [(x,y) for x in range(1,6) for y in range(6,11)]
# print(pairs)

# List Comprehension with Functions
# words = ['Sanan', 'Shaikh', 'is', 'awesome!']
# upper_case = [word.upper() for word in words]
# print(upper_case)

# List Comprehension with Nested List Comprehension
#  Flattening a 2D list

# two_dim = [[1,2],[3,4],[5,6]]
# flatten = [num for row in two_dim for num in row]
# print(flatten)

# List Comprehension with Set and Dictionary Comprehensions
#set comprehensions
# unique_num = {x for x in [1,2,3,44,44,3,2,1,6,7,8,88,88,9,0,99,9]}
# print(unique_num)

# dict comprehensions
# squares = {i : i**2 for i in range(1,6)}
# print(squares)


#performance comparison - loops vs list comprehensions

# import time
# Using a for loop
# start = time.time()
# squares_loop = []
# for x in range(10**6):
#     squares_loop.append(x**2)
# print("Loop time:", time.time() - start)
# # Using list comprehension
# start = time.time()
# squares_comp = [x**2 for x in range(10**6)]
# print("List Comprehension time:", time.time() - start)