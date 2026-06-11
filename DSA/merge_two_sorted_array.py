def sorted_merge(arr1,arr2):
    i=j=0
    result=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
obj=sorted_merge(arr1,arr2)
print("result",obj)
