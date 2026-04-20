s = input()

count = 0

for ch in s:
    if s.count(ch) == 1:
        count += 1

if count > 0:
    print(count)
else:
    print(-1)

# Problem Statement:
# Given a String S,print the number of unique characters in it.If all the characters are duplicated,then print -1.


# Sample Input:
# GUVIGEEK


# Sample Output:
# 4
