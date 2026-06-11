# Input: "I love Python"
# Output: "I evol nohtyP"

strings=input("enter the string:")
str_value=strings.split()
# print(str_value)
result=[]
for word in str_value:
    rev=""
    for ch in word:
        rev=ch+rev
    result.append(rev)
# print("result",result)
print(" ".join(result))
    