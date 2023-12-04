X = input('Enter the first string:')
Y = input('Enter the second string:')

def len(A):
    count = 0
    for i in A :    
        count+=1
    return count

def con(str1,str2):
    Z = str1 +' '+ str2
    return Z

print(len(X),len(Y))
print(con(X,Y))

