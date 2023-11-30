def perform_operations(N, A):
    operations = 0

    while all(num % 2 == 0 for num in A):
        A = [num // 2 for num in A]
        operations += 1

    return operations


N = int(input("number of element : "))
A = []
for i in range(0, N):
    A.append(int(input()))

max_operations = perform_operations(N, A)
print(f"Maximum possible operations: {max_operations}")