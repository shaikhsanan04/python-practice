# A dictionary in Python is an unordered, mutable, and key-value pair collection. It allows efficient data retrieval and modification.

# creating a dict

# empty dict
# d1 = {}

# dict with key-value pairs elements
# student = {
#     "Name" : "Sanan Shaikh",
#     "Age" : 25,
#     "Standard" : "Ninth",
#     "Grade" : "A",
#     "Roll_number" : 78 
# }

# print(student)


# using dict constructor
# person = dict(name = "Sanan", age = 25, city = "Sawantwadi")
# print(person)

# -------------------------------------------------------------------

# Accessing Dictionary Elements

# student = dict(name = "Sanan Shaikh", age = 25, std = 'PG', city = "Belgaum")

# using keys
# print(student["name"])
# print(student["age"])
# print(student["city"])
# print(student["is_passed"]) # will raise a key error

# using get() (avoids KeyError if key doesn't exist)
# print(student.get("name"))
# print(student.get("is_passed")) # will not raise an error

# -----------------------------------------------------------------

# Common dictionary methods

data = {
    "name": "Sanan",
    "age": 24,
    "city": "Mumbai",
    "profession": "Web Developer",
    "language": "Python",
    "experience_years": 2,
    "remote": True,
    "projects_completed": 15,
    "rating": 4.7,
    "learning_focus": "Data Science"
}

# keys - returns all the keys in the dict
# print(data.keys())
# print(type(data.keys()))

# values - returns all the values in the dict
# print(data.values())
# print(type(data.values()))


# items - return key value pairs as tuples
# print(data.items())
# print(list(data.items()))

# get - Returns value for key , or default if key not found.
# print(data.get("absolute_error", 55))
# print(data.get("name", "Sanan"))

# update - merges dict2 in dict 1
# add_data = {
#     "nationality" : "India",
#     "iq" : 99
# }

# data.update(add_data)
# print(data)

# pop - removes key and return its value
# name = data.pop('name') #affects the og dict
# print(f'My name is {name}')
# print()
# print()
# print(data)

# popitem - removes and return the last inserted key-value pair
# print(data.popitem()) #affects the og dict
# print()
# print()
# print()
# print(data)

# setdefault - returns the value for the key else sets it to default
# print(data.setdefault("name","Anonymous"))

# copy - returns a shallow copy
# d1 = data.copy()
# print(d1)

# clear - removes all the elements
# data.clear()
# print(data)

# ------------------------------------------------------------

# iterating over a dictionary
# for keys, values in data.items():
#     print(f"{keys} : {values}")

# ------------------------------------------------------------------------------------


# Dictionary Comprehension:

# creating a dict using comprehensions
# squares = {x : x**2 for x in range(1,101)}
# print(squares)

# -----------------------------------------


# keys = [
#     "name", "age", "city", "profession", "language",
#     "experience_years", "remote", "projects_completed",
#     "rating", "learning_focus"
# ]

# values = [
#     "Sanan", 24, "Mumbai", "Web Developer", "Python",
#     2, True, 15, 4.7, "Data Science"
# ]

# data2 = {k:v for k,v in zip(keys, values)}
# print(data2)