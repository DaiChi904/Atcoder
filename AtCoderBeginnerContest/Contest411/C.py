def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    squares: list[list[str]] = [0] * N

    for i in range(Q):
        if i != 0:
            squares.extend(squares)
        squares[(i * N) + A[i] - 1] += 1

    sum = 0
    for i in range(N * (Q + 1)):
        if i % N == 0 and i != 0:
            print(sum)
            sum = 0
            continue


main()
