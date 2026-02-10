# Q1. Data cleaning logic
# Given:
# data = ["100", "200.5", None, "NaN", "abc", 300]
# Return a list of valid floats only and compute their mean.

# ans 1
# data = ["100", "200.5", None, "NaN", "abc", 300]
# valid_floats = []
# for item in data:
#     # print(item)
#     try:
#         if item != "NaN":
#             num = float(item)
#             valid_floats.append(num)
#         else:
#             continue
#     except(ValueError, TypeError):
#         continue
# print(valid_floats)
# mean = sum(valid_floats)/len(valid_floats)
# print(f"The mean of valid floats is {mean:.2f}")


# better code
# valid = []
# for x in data:
#     try:
#         val = float(x)
#         if not math.isnan(val):
#             valid.append(val)
#     except (TypeError, ValueError):
#         pass


# Q2. Frequency analysis
# Given:
# values = ["A", "B", "A", "C", "B", "A", "D"]
# Return a dictionary of value → frequency, sorted by frequency (descending).

# ans 2
# values = ["A", "B", "A", "C", "B", "A", "D"]
# freq = {}
# for el in values:
#     if el in freq:
#         freq[el] += 1
#     else:
#         freq[el] = 1
# print(freq)
# sorted_freq = dict(
#     sorted(freq.items(), key=lambda x: x[1], reverse=True)
# )



# Q3. Sliding window (real data task)
# Given:
# nums = [10, 20, 30, 40, 50]
# Return a list of moving averages with window size = 3.
# Output:
# [20, 30, 40]

# ans 3 - Solved this using AI because I did know what moving avgs meant
# nums = [10, 20, 30, 40, 50]
# window_size = 3
# moving_avgs = []

# for item in range(len(nums) - window_size + 1):
    
#     window = nums[item : window_size + item]

#     window_avg = sum(window)/window_size
#     moving_avgs.append(float(window_avg):.2f)
# print(moving_avgs)


# Q4. Dictionary transformation
# Given:
# sales = {
#     "A": [100, 200, 300],
#     "B": [50, None, 150],
#     "C": []
# }
# Return total sales per key, skipping invalid values.

# ans 4 - I solved this with the help of AI
# sales = {
#     "A": [100, 200, 300],
#     "B": [50, None, 150],
#     "C": []
# }

# total_valid_sales = {}

# for keys, values in sales.items():
#     total = 0
#     for v in values:
#         if isinstance(v, (int, float)):
#             total += v
#     total_valid_sales[keys] = total
#     print(total)


# Q5. Grouping without pandas

# Given:

# records = [
#     ("Electronics", 1000),
#     ("Clothing", 500),
#     ("Electronics", 1500),
#     ("Food", 200),
#     ("Clothing", 800)
# ]


# Return:

# {
#   "Electronics": 2500,
#   "Clothing": 1300,
#   "Food": 200
# }

# ans 5
# records = [
#     ("Electronics", 1000),
#     ("Clothing", 500),
#     ("Electronics", 1500),
#     ("Food", 200),
#     ("Clothing", 800)
# ]

# new_records = {}

# for cat, amt in records:
#     if cat not in new_records:
#         new_records[cat] = amt
#     else:
#         new_records[cat] += amt

# print(new_records)

# Q6. Memory-safe processing (important)

# Explain with a small code example:

# How would you process a huge CSV file that cannot fit into memory?

# (Use generators or iterators.)



# ans 6 - idk



# Q7. Custom sorting (very common)
# Given:
# students = [
#     {"name": "A", "score": 90},
#     {"name": "B", "score": 75},
#     {"name": "C", "score": 90},
#     {"name": "D", "score": 60}
# ]
# Sort by:
# score descending
# name ascending (if scores are equal)

# ans 7 - using ai
# students = [
#     {"name": "A", "score": 90},
#     {"name": "B", "score": 75},
#     {"name": "C", "score": 90},
#     {"name": "D", "score": 60}
# ]

# students_sorted = sorted(students, key = lambda s : (-s["score"], s["name"]))
# print(students_sorted)
        
# Q8. Defensive function design

# Write a function that:

# Takes a list of numbers

# Returns the z-score normalized values

# Handles empty list safely

# (No NumPy.)

# ans 8
# import statistics

# def calculate_z(ls):
#     normalized = []
#     if len(ls) == 0:
#         return 0
#     else:
#         mean = statistics.mean(ls)
#         std = statistics.stdev(ls)
#         print(mean, std)
#         for x in ls:
#             z_scores = (x - mean)/std
#             normalized.append(z_scores)
#     return normalized

# print(calculate_z([1,2,3]))

# better version -

# def z_score(values):
#     if not values:
#         return []

#     mean = statistics.mean(values)
#     std = statistics.stdev(values)

#     if std == 0:
#         return [0] * len(values)

#     return [(x - mean) / std for x in values]



# Q9. Data validation
# Given:
# rows = [
#     {"age": 25, "salary": 50000},
#     {"age": -1, "salary": 40000},
#     {"age": 30, "salary": None},
#     {"age": 40, "salary": 70000}
# ]
# Return only valid rows where:
# age > 0
# salary is not None

# ans 9
# rows = [
#     {"age": 25, "salary": 50000},
#     {"age": -1, "salary": 40000},
#     {"age": 30, "salary": None},
#     {"age": 40, "salary": 70000}
# ]

# result = []

# for row in rows:
#     if(row["age"] > 0 and row["salary"] is not None):
#         obj = {
#             "age": row["age"], 
#             "salary" : row["salary"]
#         }
#         result.append(obj)
#     else:
#         continue
# print(result)


# Q10. Mini reasoning (important)

# In 2 lines max:

# Why is try/except often preferred over multiple if checks in data cleaning pipelines?
# ans 10 - because it hides the scary errors and is very effective

# Better 2-line answer:

# Because real-world data is unpredictable, and try/except lets pipelines continue processing without breaking on bad records, while keeping validation logic concise.