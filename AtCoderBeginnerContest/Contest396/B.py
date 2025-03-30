def main():
    initialArray = list(0 for _ in range(100))

    Q = int(input())
    q = [list(map(int, input().split())) for l in range(Q)]

    for i in range(Q):
        if q[i][0] == 1:
            initialArray.append(q[i][1])
        if q[i][0] == 2:
            print(initialArray.pop(-1))

main()
