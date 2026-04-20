s = input()

words = s.split()

result = ""

for w in words:
    result += w.capitalize()

print(result)