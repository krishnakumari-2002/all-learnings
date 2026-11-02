import textwrap

def wrap(string, max_width):
    u=" "
    for i in range(0,len(string),max_width):
        u+=string[i:i+max_width]+"\n"
    return u

if __name__ == '__main__':
    string, max_width = input("Enter the string:"), int(input("Enter the max_width:"))
    result = wrap(string, max_width)
    print(result)