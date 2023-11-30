
n = int(input("enter the length of array"))
A = []
for i in range(0, n):
    element = int(input())
    
    A.append(element)

print('='*40)
for i in range(0,n):
    for j in range(i,n):
        arr = []

        for x in range(i,j+1):
            arr.append(A[x])

        print(max(arr))