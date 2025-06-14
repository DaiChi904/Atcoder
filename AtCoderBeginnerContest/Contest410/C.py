def main():
    N, Q = map(int,input().split()) 
    queries = [list(map(int, input().split())) for _ in range(Q)]

    A: list[int] = []
    for i in range(N):
        A.append(i + 1)

    offset = 0

    for query in queries:
        if query[0] == 1:
            idx = (query[1] - 1 + offset) % N
            A[idx] = query[2]
        elif query[0] == 2:
            idx = (query[1] - 1 + offset) % N
            print(A[idx])
        elif query[0] == 3:
            offset = (query[1] + offset) % N

main()
