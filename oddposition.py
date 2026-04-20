name=input("")
odd=""
even=""
result=""
for index,value in enumerate(name,start=1):
    if index % 2 != 0:
        odd=odd+value
    else:
        even=even+value
result = odd +" "+ even
print(result)


# Given a string S, print 2 strings such that first string containing all characters in odd position(s) and other containing all characters in even position(s).


# Sample Input:
# XCODE


# Sample Output:
# XOE CD

