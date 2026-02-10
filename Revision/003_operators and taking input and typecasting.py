# Operators

# 1. Arithmetic Operators Used for basic mathematical operations.

# + Addition a + b # 15
# - Subtraction a - b # 5
# * Multiplication a * b # 50
# / Division a / b # 2.0
# // Floor Division a // b # 2
# % Modulus a % b # 0
# ** Exponentiation a ** b # 100000

# examples - 
# print(12 + 5)
# print(12 - 5)
# print(12 * 5)
# print(12 / 5)
# print(12 // 5)
# print(12 % 5)
# print(2 ** 5)

# 2. Comparison Operators

# Compare values and return True or False .

# == Equal to a == b # False
# != Not equal to a != b # True
# > Greater than a > b # True
# < Less than a < b # False
# >= Greater or equal a >= b # True
# <= Less or equal a <= b # False

# examples - 
# a = 12 
# b = 15
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a <= b)
# print(a >= b)

# 3. Logical Operators

# Used to combine conditional statements.

# and Both True x and y # False
# or Either True x or y # True
# not Negation not x # False

# examples -
# x,y = True, False
# print(x and y)
# print(x or y)
# print(not x)
# print(not y)

# 4. Bitwise Operators

# Perform bit-level operations.

# & AND a & b # 1
# \| OR a \| b # 7

# 5. Assignment Operators

# Used to assign values to variables.

# += a += 5 a = a + 5
# -= a -= 5 a = a - 5
# *= a *= 5 a = a * 5
# /= a /= 5 a = a / 5
# //= a //= 5 a = a // 5
# %= a %= 5 a = a % 5
# **= a **= 5 a = a ** 5

# examples  -
# a = 2
# a += 2
# a -= 2
# a *= 2
# a /= 2
# a //= 2
# a **= 2
# a %= 2
# print(a)

# 6. Membership & Identity Operators
# Check for presence and object identity.
    
# in Present in sequence x in lst # True
# not in Not present x not in lst # False
# is Same object a is b # False
# is not Different object a is not b # True

# examples - 
# name = "Sanan is a middle class man"
# new_name = "In Future Sanan is a rich man"

# print("Sanan" in name)
# print("Sanan" not in name)
# print(new_name is name)
# print(new_name is not name)

# -------------------------------------------------------------------


# Taking input from the user

# name = input("Enter your Name : ")
# print(name)

# NOTE - input always returns a string

# Type Conversion
age = int(input('Enter your age : '))
print(age)
print(type(age))


# Operator Precedence
# Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction). The order of operations in Python is:

# Parentheses () – Highest precedence, operations inside parentheses are evaluated first.
# Exponents ** – Power calculations (e.g., 2 ** 3 → 8).
# Multiplication * , Division / , Floor Division // , Modulus % – Evaluated from left to right.
# Addition + , Subtraction - – Evaluated from left to right.
