text=input().split()
count=0
for i in text[0]:
    if text[1] in i:
        count=count+1
if count>=1:
    print(count)
else:
    print("-1")

Problem Statement:
Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1


Input Description:
The input consists of a string 'S' and a character 'K'. The size of string 'S' is at most 100000.


Output Description:
The output is the count of character 'K' in string 'S'. If 'K' is not found, print -1.


Sample Input:
codekata a


Sample Output:
2    