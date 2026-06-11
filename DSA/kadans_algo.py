def kadans_algorithm(arr):
    current_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        current_sum=max(arr[i],arr[i]+current_sum)
        max_sum=max(current_sum,max_sum)
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj=kadans_algorithm(arr)
print("value",obj)