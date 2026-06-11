def swap(s):
    d=" "
    for i in s:
        if i.isupper():
            d+=i.lower()
        elif i.islower():
            d+=i.upper()
        else:
            d+=i
    return d

s="HelLO"
result=swap(s)
print('result',result)