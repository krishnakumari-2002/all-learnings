# arr = [10, 5, 8, 20, 15]
# largest=float('-inf')
# second_largest=float('-inf')
# for i in arr:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest and i!=largest:
#         second_largest=i
# print(second_largest)


arr = [10, 5, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    elif largest > i > second_largest:
        second_largest = i

print(second_largest)
        