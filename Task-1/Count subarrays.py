def count_non_decreasing_subarrays(N, A):
    count = 0
    prev = float('-inf')

    for num in A:
        count += 1

        if num < prev:
            count = 1

        prev = num

    return count


N = int(input("enter the number of element : "))
A = []
for i in range (0, N):
    A.append(int(input()))
num_subarrays = count_non_decreasing_subarrays(N, A)
print(f"Number of non-decreasing subarrays: {num_subarrays}")