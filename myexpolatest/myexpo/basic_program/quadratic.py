import math

a=float(input("enter the a value:"))
b=float(input("enter the b value:"))
c=float(input("enter the c value:"))

d=b**2 - 4*a*c
print("d",d)
if d>0: #if the d value is greated then 0
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("root1",root1)
    print("root2",root2)
elif d==0: #if d value is equal to the 0
    root=-b/(2*a)
    print("root",root)
else: #other vise it was an negative values like less than the 0
    realpart=-b/(2*a)
    imaginarypart=math.sqrt(abs(d))/(2*a)
    print(f"root1 {realpart}+ {imaginarypart}i")
    print(f"root2 {realpart}- {imaginarypart}i")
    
    
    
#a=1,b=-3,c=2 answer will be x₁ = 2, x₂ = 1 (1st scenario)
#a=1,b=-2,c=1 answer will be x = 1 (2nd scenario)
#a=1,b=2,c=5 answer will be x₁ = -1 + 2i, x₂ = -1 - 2i (3rd scenario)

x=-b± root of b2−4ac/2a
​​