arr = [10, 5, 8, 20, 15]

small = float("inf")
very_small = float("inf")

for i in arr:
    if i < small:
        very_small = small
        small = i
      
    elif small < i < very_small:
        very_small = i

print(very_small)   