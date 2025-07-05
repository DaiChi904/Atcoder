def main():
    N = int(input())
    S = [str(input()) for _ in range(N)]

    res: set[str] = set()

    for i in range(N):
        for j in range(N):
            if (i == j):
                continue

            _S = S[i] + S[j]
            res.add(_S)

    print(len(res))

main()
