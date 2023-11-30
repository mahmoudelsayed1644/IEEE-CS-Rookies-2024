n = int(input("enter number of element: "))
m = []
for i in range(n):
    m.append(int(input()))

max = m.index(max(m))
min = m.index(min(m))
def swap(m,max,min):
    temp = m[max]
    m[max] = m[min]
    m[min] = temp

swap (m,max,min)
print(m)