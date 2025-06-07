def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    res = 1

    for num in A:
        res *= num
        if len(str(res)) > K:
            res = 1

    print(res)

main()
