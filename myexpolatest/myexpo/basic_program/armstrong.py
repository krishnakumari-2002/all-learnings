def armstrong():
    number=int(input("enter the number:"))
    num=str(number)
    num_len=len(num)
    sum=0
    print('len',num_len)
    for _ in range(num_len):
        a=number%10
        sum+=a**num_len
        number=number//10
    return sum

obj=armstrong()
print("-----------",obj)


# num = int(input("Enter a number: "))  # User enters 153
# sum = 0                                # Initialize sum to 0
# temp = num                             # temp = 153
# digits = len(str(num))                 # Count number of digits, digits = 3

# while temp > 0:                        # Loop until temp becomes 0
#     digit = temp % 10                  # Get last digit
#     sum += digit ** digits             # Add digit^digits to sum
#     temp //= 10                        # Remove last digit

# if num == sum:                         # Compare original number with sum
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")
