if __name__ == '__main__':
    i = input("enter the string:")
    a=b=c=d=e=False
    for s in i:
        if s.isalnum():
            a=True
        if s.isalpha():
            b=True
        if s.isdigit():
            c=True
        if s.islower():
            d=True
        if s.isupper():
            e=True
        
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
