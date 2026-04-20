text=input().split()
for index,value in enumerate(text[0],start=1):
    if text[1] in value:
        print(index)
        break
else:   
    print("-1")


# Problem Statement:
# Given a string 'S' and a character 'K', find at what position the character 'K' occurs for the first time in 'S'.(Assume the index of string starts at 1).If the character is not found in 'S' then print -1


# Input Description:
# Input Size : |s| <= 100000


# Sample Input:
# codekata a


# Sample Output:
# 6
