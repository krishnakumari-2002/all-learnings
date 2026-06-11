strings = "a1b10"
result = ""
i = 0

while i < len(strings):
    if strings[i].isalpha():
        ch = strings[i]
        i += 1
        num = ""

        while i < len(strings) and strings[i].isnumeric():
            num += strings[i]
            i += 1

        result += ch * int(num)

print(result)
