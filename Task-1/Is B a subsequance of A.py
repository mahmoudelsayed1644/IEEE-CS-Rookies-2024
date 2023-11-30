N = int(input("enter the number of element in arr1 : "))
M = int(input("enter the number of element in arr2 : "))
list_1 = []
list_2 = []
for i in range(0,N):
    list_1.append(int(input()))
for i in range(0,M):
    list_2.append(int(input()))

def is_subsequence(N, M, List_1, List_2):
    ptrlist_1 = 0
    ptrlist_2 = 0

    while ptrlist_1 < N and ptrlist_2 < M:
        if list_1[ptrlist_1] == list_1[ptrlist_2]:
            ptrlist_1 += 1
            ptrlist_2 += 1
        else:
            ptrlist_1 += 1

    return ptrlist_2 == M