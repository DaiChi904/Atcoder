def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]

    protected: list[int] = [0] * (N + 1)

    for L, R in LR:
        protected[L - 1] += 1
        protected[R] -= 1

    for i in range(1, N):
        protected[i] += protected[i - 1]

    print(min(protected[:-1]))

main()
