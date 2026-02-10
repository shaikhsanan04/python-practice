# if-elif-else
# eg 1
# age = 225
# if(age >= 18 and age <=100):
#     print("He can vote")
# elif(age > 100):
#     print("You are not a human")
# else:
#     print("He cannot vote")


# eg 2
# age = 15

# if age < 18:
#     category = "Minor"
# elif age <=65 :
#     category = "Adult"
# else:
#     category = "Senior Citizen"

# print(f"category : {category}")

# --------------------------------------------------------------


# Match Case Statements

# The match-case statement, introduced in Python 3.10, provides pattern matching similar to switch statements in other languages.

# day = int(input("Enter the day from 1-7 : "))

# match(day):
#     case 1:
#         print("Sunday")
#     case 2:
#         print('Monday')        
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("No day exist!")



# --------------------------------------------

# Formatting Numbers
pi = 3.14159
print(f"the value of pi is {pi:.3f}")


# Padding and Alignment
# print(f"{'Python':<10}") # Left-align
# print(f"{'Python':>10}") # Right-align
# print(f"{'Python':^10}") # Center-align
