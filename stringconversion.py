name=input()
result=""
for i in name:
    if i.islower():
        result=result+i.upper()
    elif i.isupper():
        result=result+i.lower()
    else:
        result=result+i
print(result)        


# Problem Statement:
# Given a string S change upper case to lowercase and lowercase to uppercase.


# Input Description:
# The input consists of a string S with size |s| <= 10000000 (complexity O(n)).


# Sample Input:
# CodEkaTa


# Sample Output:
# cODeKAtA