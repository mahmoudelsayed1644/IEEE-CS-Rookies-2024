
#list = [5,3,7,2,8]

#n = len(list)
#for i in range(n-1):
    #for j in range(i+1,n):
       # if list[j] < list[i]:
            #temp = list[i]
           # list[i] = list[j]
          #  list[j] = temp
#print(list)

t = int(input("plese enter the number: "))
n = int(input("enter number of element: "))
m = []
for i in range(n):
    m.append(int(input()))
min = m[0]+m[1]+1

for i in range(1,n-1):
    for j in range(i+1,n):
        sum = m[i]+m[j]+j-i
        if sum < min :
            min = sum 
print(min)