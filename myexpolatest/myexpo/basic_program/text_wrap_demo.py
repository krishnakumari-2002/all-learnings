import textwrap 
def wrap(string, max_width): 
    return textwrap.fill(string,max_width) 

if __name__ == '__main__': 
    string, max_width = input("Enter the string:"), int(input("Enter the max_width:"))
    result = wrap(string, max_width) 
    print(result)