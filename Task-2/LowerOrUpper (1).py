str1 = input()

result = ""
for i in range(len(str1)):
    if(str1[i].isupper()):
        result += str1[i].lower()
print(result)