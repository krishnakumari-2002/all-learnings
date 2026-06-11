def rain_water(arr):
    left=1
    right=len(arr)-2
    res=0
    lmax=arr[left-1]
    rmax=arr[right+1]

    while left<=right:
        if rmax<=lmax:
            res+=max(0,rmax-arr[right])
            rmax=max(rmax,arr[right])
            right-=1
        else:
            res+=max(0,lmax-arr[left])
            lmax=max(lmax,arr[left])
            left+=1
    return res

arr=[2, 1, 5, 3, 1, 0, 4]
obj=rain_water(arr)
print(obj)