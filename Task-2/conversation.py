X = input()
# X = X.replace(',',' ')
# X = X.swapcase()
# print(X)

# is_lower()
# is_upper()
def dd(X):
    for i in range(len(X)):
        if(X[i].isupper()):
            X[i].lower()
    


print(dd(X))

