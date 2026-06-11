N, M = map(int, input().split())

pattern = '.|.'

# Top part
for i in range(N//2):
    print((pattern * (2*i + 1)).center(M, '-'))

# Middle
print('WELCOME'.center(M, '-'))

# Bottom part
for i in range(N//2 - 1, -1, -1):
    print((pattern * (2*i + 1)).center(M, '-'))



# input=9 27    Mat size must be NXM. ( N is an odd natural number, and M is  3times N .)
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------