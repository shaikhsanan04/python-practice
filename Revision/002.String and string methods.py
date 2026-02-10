# A string is a sequence of characters enclosed in single ( ' ) or double ( " ) quotes.

# singleline_string = "Sanan is a badass"
# print(singleline_string)


# multiline_string = """
# Sanan is a 
# badass guy
# with a beautiful heart.
# """
# print(multiline_string)


# ----------------------------------------------


# String Indexing and Slicing
# text = 'Sanan'
# print(text[0]) # prints S
# print(text[-1]) # prints n
# print(text[0:2]) # Prints Sa
# print(text[:3]) # Prints San
# print(text[3:]) # prints an

# String Immutability - Strings cannot be changed after creation
# name = 'Sanan'
# name[0] = 'K'
# print(name) 
# will give a typeError because string is immutable. which means Once we create a string, the stribng or its characters cannot be updated

# -----------------------------------------------------------------------------

# common string methods
# name = "Sanan"
# print(f'{name} in lower case is {name.lower()}')
# print(f'{name} in upper case is {name.upper()}')
# print(f'{name} in title case is {name.title()}')

# x = "   shaikh_sanan_007   "
# xx = x.strip()
# print(xx)

# old = "Arsalan is the new king of the Jungle!"
# new = old.replace('Arsalan','Sanan')
# print(new)

# new_string = "Sanan is a candyman"
# listed = new_string.split(" ")
# print(listed)

# new_list = ["Apple","Mango","Grapes","Banana"]
# y = " ".join(new_list)
# print(y)

# string = "My name is Khan and I am not a Terrorist. Also my last is Khan so I am Khan Khan Khan khan"
# found = string.find("Khan")
# print(found)

# counted = string.count("Khan")
# print(counted)

# print(string.startswith('a'))
# print(string.startswith('m'))
# print(string.startswith('M'))

# print(string.endswith('a'))
# print(string.endswith('m'))
# print(string.endswith('n'))

# xc = "12345"
# xcc = "Sanan is not a digit but contains a digit 007"
# print(xc.isdigit())
# print(xcc.isdigit())

# print(xc.isalpha())
# print(xcc.isalpha())

# print(xc.isalnum())
# print(xcc.isalnum())

# ---------------------------------------------------------------------

# String Formatting (F-Strings)

name = "Sanan"
age = 25
interest = ["coding", "riding bikes"]


print(f"My name is {name} and my age is {age} and my interests are {interest}")