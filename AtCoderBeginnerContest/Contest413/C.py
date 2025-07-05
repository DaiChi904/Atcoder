# うーんよくわからん
def dfs(A: list[int], B: list[int], currentIdx: int, remaining: int) -> int:
    res = 0
    tempRemaining = B[currentIdx] - remaining
    if (tempRemaining <= 0):
        res = A[currentIdx] * B[currentIdx]
        B[currentIdx] = 0
        currentIdx += 1
        return res + dfs(A, B, currentIdx, -tempRemaining)

    if (tempRemaining > 0):
        B[currentIdx] = tempRemaining
        res = A[currentIdx] * remaining
        return res

def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    A: list[int] = []
    B: list[int] = []

    currentIdx = 0

    for query in queries:
        if query[0] == 1:
            c = query[1]
            x = query[2]
            A.append(x)
            B.append(c)

        if query[0] == 2:
            k = query[1]
            res = dfs(A, B, currentIdx, k)
            print(res)

main()

