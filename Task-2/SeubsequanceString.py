def check_subsequence(s):
    M = "hello"
    i = 0

    for char in s:
        if char == M[i]:
            i += 1
            if i == len(M):
                return "YES"
    
    return "NO"

s = input()
result = check_subsequence(s)
print(result)