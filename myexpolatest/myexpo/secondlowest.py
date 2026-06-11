# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

# 26.50

if __name__ == '__main__':
    data=[]
   
    for _ in range(int(input("enter the count:"))):
        name = input("enter the name:")
        marks=[]
        for i in range(3):
            score = float(input("enter the score:"))
            marks.append(score)
        data.append([name,marks])
        print("data",data)
        
    for student in data:
        name = student[0]
        scores = " ".join(str(int(m)) for m in student[1])
        print(name, scores)
    
            
            