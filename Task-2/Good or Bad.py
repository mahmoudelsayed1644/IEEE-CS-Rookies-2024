no_of_iterations = int(input("enter No of iterations:"))
arr1 = []
for i in range(no_of_iterations):
    X = input()
    arr1.append(X)

def dd(str1) :
    check1 = '010'
    check2 = '101'

    substrings = [str1[i:i+3] for i in range(0, len(str1), 3)]

    for subString in substrings:
        if(subString == check1 or subString == check2):
            return 'good'
        
    return 'Bad'
        

for j in range(no_of_iterations):
    print(dd(arr1[j]))



