name = input().split()

s1 = name[0]
s2 = name[1]

result = ""

for i in s1:
    if i not in s2:
        result += i

if result == "":
    print(-1)
else:
    print(result)

# Problem Statement:
# Given a string two strings S1 and S2, remove characters from the S1 which are present in the S2.If S1 becomes empty then print -1


# Input Description:
# Input Size : N <= 100000


# Sample Input:
# GUVI GEEK


# Sample Output:
# UVI    