# Opening a File and Reading a file

# read - Reads the entire file at once, Returns one single string
# file = open("files/calorie.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)

# readline - Reads one line at a time, Each call reads the next line
# file = open("files/calorie.txt", "r", encoding="utf-8")
# content = file.readline()
# print(content)

# readlines - Reads all lines at once, Returns a list of strings, Each line is an element in the list
# file = open("files/calorie.txt", "r", encoding="utf-8")
# content = file.readlines()
# print(content)


# file = open("C:/users/sanan/downloads/sanan.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)

# -------------------------------------------------------------------------------------------------------

# Writing to a file

# write() - overwrites file if file exist

# writing to a file that we already created 
# file = open("files/demo.txt","w",encoding="utf-8")
# content = "Hello My name is Sanan Shaikh and I am the lowest best in the world."
# if file.write(content):
#     print("Written Successfully")
# else:
#     print("Failed to write in the file")


# writing to a file that we will create while writing the code
# file = open("files/sandy.txt","w",encoding="utf-8")
# content = "Hey there I am using whatsapp."
# if file.write(content):
#     print("Mission successfull")
# else:
#     print('Mission Failed')


# Using writelines() – Write Multiple Lines

# lines = ["Hello\n", "We are working with files now\n", "We can read, write and append new content to files\n",  "isn't that awesome?\n", "I hope you like this tutorial"]

# file = open("files/newfile_for_writelines.txt","w", encoding="utf-8")
# file.writelines(lines)

# -------------------------------------------------------------------------------------


# Appending to a file

# file = open("files/app.txt","a",encoding="utf-8")
# con = "\nHe is a very underrated person, Who has a lot of skills"
# file.write(con)
# file.close()

# ----------------------------------------------------------------------------------------

# Using with Statement (Best Practice)
# using with open() ensures files automatically close after execution

# with open("files/fear.txt","r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# ----------------------------------------------------------------------------------------

# Checking if a File Exists
# Use the os module to check if a file exists before opening it.

# import os

# if os.path.exists("c:/users/sanan/downloads/calorie.docx"):
#     print('File Exist')
# else:
#     print('File does not exist')


# use the os module to delete a file

# if os.path.exists("c:/users/sanan/downloads/sanan.txt"):
#     os.remove("c:/users/sanan/downloads/sanan.txt")
#     print('File Deleted!')
# else:
#     print("File does not exist")

# ----------------------------------------------------------------------------------------

# Working with Binary Files
# Binary files ( .jpg , .png , .pdf , etc.) should be opened in binary mode ( 'b' ).

# with open("c:/users/sanan/downloads/PF CLAIM 3.pdf", "rb") as file:
#     data = file.read()
#     print(data)

# ----------------------------------------------------------------------------------------

# JSON module in Python

# JSON (JavaScript Object Notation) is a lightweight data format used for data exchange between servers and applications. It is widely used in APIs, web applications, and configurations.

# Python provides the json module to work with JSON data. You can import the json module like this:

import json

# Converting Python Objects to JSON (Serialization)
# Serialization (also called encoding or dumping) is converting a Python object into a JSON-formatted string.

# json.dumps() – Convert Python object to JSON string

# data = {
#     "name" : "Sanan",
#     "age" : 25,
#     "weight" : 75.75    
# }

# json_string = json.dumps(data, indent = 4)
# print(json_string)
# print(type(json_string))
# print(type(data))

# dump() - write json data to a file
# with open("files/data.json", "w") as file:
#     json.dump(data, file)

# Converting JSON to Python Objects (Deserialization)
# Deserialization (also called decoding or loading) is converting JSON-formatted data into Python objects.

# json.loads() – Convert JSON string to Python object

# json_data = '{"name":"Sandy", "age": 25, "profession": "Doctor"}'
# print(type(json_data))

# pyt_pbj = json.loads(json_data)
# print(pyt_pbj)
# print(type(pyt_pbj))

# json.load() - reads json data from a file
# with open("files/data.json","r", encoding="utf-8") as file:
#     content = json.load(file)
#     print(content)
#     print(type(content))

