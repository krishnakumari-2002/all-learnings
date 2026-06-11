def factorial():
    num=int(input("enter the factorial number:"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
obj=factorial()
print("obj",obj)    