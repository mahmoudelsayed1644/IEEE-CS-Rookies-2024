N = int(input("enter number of elements : "))
list_1 = []
list_2 = []
for i in range(0, N):
    list_1.append(int(input()))
    list_2.append(int(input()))

def is_permutation(N, list_1, list_2):
    if len(list_1) != len(list_2):
        return False

    frequency = {}

    for num in list_1:
         if num in frequency:
            frequency[num] += 1
    else:
            frequency[num] = 1


    for num in list_2:
        if num not in frequency or frequency[num] == 0:
            return False
        else:
            frequency[num] -= 1


    if any(frequency.values()):
        return False

    return True

