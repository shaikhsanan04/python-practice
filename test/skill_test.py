# Section 1: Core Python (must-have)

# Q1.Given:
# data = [10, 15, None, 20, "25", "bad", 30]
# Write code to:
# Remove invalid values
# Convert valid numbers to integers
# Return the mean

# Ans 1 - 
# data = [10, 15, None, 20, "25", "bad", 30]
# clean_data = []
# for item in data :
#     try:
#         num = int(item)
#         clean_data.append(num)
#     except(ValueError, TypeError):
#         continue
# print(f"The cleaned list is {clean_data}")

# if len(clean_data) > 0:
#     mean_val = sum(clean_data)/len(clean_data)
# print(f"the mean of the above cleaned list is {mean_val}")



# Q2. Write a function that takes a list of numbers and returns:
# mean
# median
# standard deviation
# You may not use NumPy.

# ans 2
# import statistics
# def stats(ls):
#     mean = statistics.mean(ls)
#     median = statistics.median(ls)
#     std = statistics.stdev(ls)
    
#     return mean, median, std

# print(stats([1,2,3,4,5,6]))

# Q3.
# Given:
# records = [
#     {"name": "A", "score": 80},
#     {"name": "B"},
#     {"name": "C", "score": None},
#     {"name": "D", "score": 90}
# ]
# Return a dictionary of names and scores, skipping invalid scores.

# ans 3
# records = [
#     {"name": "A", "score": 80},
#     {"name": "B"},
#     {"name": "C", "score": None},
#     {"name": "D", "score": 90}
# ]

# result = {}
# for r in records:
#     if r.get("score") is not None:
#         result[r["name"]] = r["score"]
# print(result)


# Section 2: Pythonic thinking (important)

# Q4.
# Using a single list comprehension, return squares of even numbers from:
# nums = range(1, 21)

# ans 4
# nums = range(1,21)
# squares_even = [i**2 for i in nums if i%2 == 0]
# print(squares_even)

# Q5.
# Explain (in one or two lines):
# When would you prefer a generator over a list in data science?
# ans 5 - Use a generator when working with large datasets or streams where loading everything into memory at once is inefficient. Generators compute values lazily and save memory.
# Example:
# (x*x for x in range(10**9))


# Section 3: File handling (real-world)

# Q6.
# Write code to safely read a CSV file and handle the case where:
# The file does not exist
# The file is empty
# (No pandas allowed)

# ans 6
# import csv
# filename = 'sanan_new_data.csv'

# try:
#     with open(filename, "r", encoding="utf-8") as file:
#         reader = csv.reader(file)
#         data = list(reader)
#         if not data:
#             print("File is Empty") 
#         else:  
#             for row in data:
#                 print(row)
# except(FileNotFoundError):
#     print("File not found!")


# Section 4: Functions & reuse (very important)

# Q7.
# Write a function that:
# Takes a list
# Returns a new list with duplicates removed
# Preserves original order

# ans 7
# def preserves(ls):
#     new_ls = []
#     for i in ls:
#         if i not in new_ls:
#             new_ls.append(i)
#     print(new_ls)
# preserves([1,1,2,2,3,3,3,3,4,5,6,7,10,45,65,4,4,6,6,89,78,45,32])
# preserves([11,22,33,33,22,44,11,55,22,33])
# preserves([12,24,21,23,21,24,23,23,23,11,11,12,12])



# Section 5: Error handling & robustness

# Q8.
# Given:
# values = ["10", "20", "x", None, "30"]
# Write code that:
# Converts valid values to integers
# Skips invalid values
# Does not crash

# ans 8
# values = ["10", "20", "x", None, "30"]

# new_refined = []
# for value in values:
#     try:
#         num = int(value)    
#         new_refined.append(num)
#     except(ValueError, TypeError):
#         continue

# print(new_refined)


# Section 6: Mini logic (data-style thinking)

# Q9.
# You receive daily sales data as a list of tuples:
# sales = [("2024-01-01", 200), ("2024-01-02", 0), ("2024-01-03", -50), ("2024-01-04", 300)]
# Return only valid sales days (sales > 0).

# ans 9
# sales = [("2024-01-01", 200), ("2024-01-02", 0), ("2024-01-03", -50), ("2024-01-04", 300)]

# refined_sales = []
# for sale in sales:
#     # print(sale)
#     if sale[1] > 0:
#         refined_sales.append(sale)
# print(refined_sales)

# Final question (important)

# Q10.
# In 2–3 lines:
# What makes Python suitable for data science compared to other languages?

# ans 10
# In python, we have vast number of useful libraries that can be used for data science. Most of the people in industry uses python as theri first choice for data science. we can also use R. some popular libraries we use for data science provided by pyhton are - numpy, pandas, matplotlib, and many more.

# Stronger version:

# Python is widely used in data science due to its rich ecosystem of libraries, simple syntax, and strong community support. It allows rapid prototyping, data analysis, and integration with ML and deployment tools.