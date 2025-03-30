N = int(input())

S = [str(input()) for _ in range(N)]

S.sort(key = len)

joinedS = "".join(S)

print(joinedS)
