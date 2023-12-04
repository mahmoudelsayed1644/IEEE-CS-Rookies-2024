def maximum_subsequence_size(N, S):
    M = [0] * N
    M[0] = 1

    for i in range(1, N):
        if S[i] != S[i-1]:
            M[i] = M[i-1] + 1
        else:
            M[i] = M[i-1]

    return M[N-1]

N = int(input())
S = input()

result = maximum_subsequence_size(N, S)
print(result)