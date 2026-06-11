# ----------------question number1------------------
# Changing dictionary keys (fname → firstname, lname → lastname)
# Original list of dictionaries
# data = [
#     {"fname": "krishna", "lname": "kumar", "age": 55, "id": 5},
#     {"fname": "ram", "lname": "raj", "age": 30, "id": 6}
# ]

# # New list to store ordered dictionaries
# new_data = []

# for d in data:
#     new_dict = {
#         "firstname": d["fname"],
#         "lastname": d["lname"],
#         "age": d["age"],
#         "id": d["id"]
#     }
#     new_data.append(new_dict)

# # Print final output
# print(new_data)



# # ---------------------2-------------
# # Finding pairs whose sum equals target
# nums = [1, 2, 3, 4, 5]
# target = 5

# pairs = []

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             pairs.append((nums[i], nums[j]))

# print(pairs)

# # -----------------3-------------
# # Maximum product of three numbers
# Input list
# nums = [1, 10, -5, 1, -100]

# # Step 1: Sort the list
# nums.sort()

# # Step 2: Product of three largest numbers
# product1 = nums[-1] * nums[-2] * nums[-3]

# # Step 3: Product of two smallest and the largest number
# product2 = nums[0] * nums[1] * nums[-1]

# # Step 4: Get maximum product
# max_product = max(product1, product2)

# # Output
# print("Sorted list:", nums)
# print("Product of largest three numbers:", product1)
# print("Product of two smallest and largest:", product2)
# print("Maximum product of three numbers:", max_product)





# -----------4--------------
# Printing only firstname from list of dicts
# data = [
#     {'firstname': 'krishna', 'lastname': 'kumar', 'age': 55, 'id': 5},
#     {'firstname': 'rajeshwari', 'lastname': 'raj', 'age': 30, 'id': 6}
# ]
 
# for d in data:
#     print(d['firstname'])
    
    
    
# # -------------5-------------
# # Converting string price to int + adding taxfor item in data:
# data = [
#     {"id": 1, "price": "1000"},
#     {"id": 2, "price": "2500"}
# ]
 
# for item in data:
#     # convert price from string to int
#     price = int(item["price"])
    
#     # calculate 18% tax
#     tax = price * 0.18
    
#     # add tax to price
#     total_price = price + tax
    
#     # update dictionary
#     item["price"] = price
#     item["price_with_tax"] = total_price
 
# print(data)

# ------------6-------------------
# Default mutable argument problem (VERY IMPORTANT)

def my_func(x, y=[]):
    y.append(x)
    return y

print(my_func(1))
print(my_func(2))
print(my_func(3))

