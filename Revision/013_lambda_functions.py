# A lambda function in Python is an anonymous, single-expression function defined using the lambda keyword. It is commonly used for short, throwaway functions where a full function definition is unnecessary.


# Simple Lambda Function
# square = lambda x : x ** 2
# print(square(10))

# Using Lambda Functions with map() , filter() , and reduce()

# Using map() with Lambda
# Applies a function to each element of an iterable.

# nums = [1,2,3,4,5]
# squared = list(map(lambda x : x**2, nums))
# print(squared)

# Using filter() with Lambda
# Filters elements based on a condition.
# nums = [1,2,3,4,5,6,7,8]
# filtered = list(filter(lambda x : x%3 ==0, nums))
# print(filtered)

# Using reduce() with Lambda
# Reduces an iterable to a single value (requires functools.reduce ).
# from functools import reduce
# nums = [1,2,3,4,60]
# reduced_value = reduce(lambda x,y : x * y, nums)
# print(reduced_value)

# Lambda with Multiple Arguments
# Adding Two Numbers
# add = lambda x,y,z : x + y + z
# print(add(1,2,3))

# finding the max of two numbers
max = lambda x,y : x if x > y else y
print(max(45,65))
