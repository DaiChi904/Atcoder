s = input().split()
N = int(s[0])
M = int(s[1])
A = list(map(int, input().split()))

R = []

T = []

for i in range(N):
    R.append(i + 1)

for i in range(M):
    R.remove(A[i])

R_str = [ str(a) for a in R]
Result = ' '.join(R_str)

print(len(R))
print(Result)
