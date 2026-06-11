def mutate_string(string, position, character):
    return f"{string[:position]}{character}{string[position+1:]}"
if __name__ == '__main__':
    s = input("Enter the string:")
    i, c = input("enter the index and char:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)