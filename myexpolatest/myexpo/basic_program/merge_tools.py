#Break the string into chunks of size k and print unique characters from each chunk in the same order.

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i + k]
        print("part",part)
        u = ""
        for ch in part:
            # print("ch",ch)
            if ch not in u:
                u += ch
        print(u)


if __name__ == '__main__':
    string = input("Enter the string:")
    k = int(input("Enter the intger value:"))
    merge_the_tools(string, k)




# def merge_the_tools(string, k): 
#     u=" " 
#     str_len=len(string) 
#     print("str",str_len) 
#     div=str_len//k 
#     print("div",div) 
#     for i in range(str_len): 
#         for j in range(div): 
#             if string not in u: 
#                 u+=" ".join(string) 
#     return u 
# if __name__ == '__main__': 
#     string, k = input("enter the string:"), int(input("enter the k value:")) 
#     obj=merge_the_tools(string, k)