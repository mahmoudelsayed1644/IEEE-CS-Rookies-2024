A = int(input("please enter A"))
B = int(input("please enter B"))
print("please enter the code")

S = []
for i in range(0, A+B+1):
    element = input()
    # adding the element
    S.append(element)

flag = 0
digits = ['0','1','2','3','4','5','6','7','8','9']


for i in range(0,len(S)):

    if(i == A):

        if(S[i] != '-'):
            flag = 1
            break
        continue

    if not(S[i] in digits):
        flag = 1
        break

if(flag == 1):
    print("No")
else:
    print("Yes")