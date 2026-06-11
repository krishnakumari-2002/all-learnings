p= "python is easy"
rev=" "
s=p.split()
for i in s:
    rev=i+" "+rev
print(rev.strip())
