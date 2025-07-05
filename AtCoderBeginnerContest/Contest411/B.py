def main():
    N = int(input())
    D = list(map(int, input().split()))

    for i in range(N - 1):
        res: list[int] = []
        cumulativeSum = 0
        for j in range(i, N - 1):
            cumulativeSum += D[j]
            res.append(cumulativeSum)

        res = [str(a) for a in res]
        print(" ".join(res))

main()
