# The function reverses elements between the given start and end indexes by swapping elements in-place while moving toward the center
# ------------method1-------------
def reverse_between(arr, start, end):
    for i in range((end - start + 1) // 2):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
    return arr


# ----------method2----------------

# def reverse_between(arr, start, end):
#     for i in range((end - start + 1) // 2):
    #     arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
    # return arr


# Example input
arr = [1, 2, 3, 4, 5]
start = 1
end = 3

# Function call
result = reverse_between(arr, start, end)

# Output
print(result)
