def main():
    N = int(input())
    AB = [list(map(int, input().split())) for l in range(N)]

    cnt = 0

    for i in range(N):
        target = AB[i][0]
        actual = AB[i][1]

        if target < actual:
            cnt += 1

    print(cnt)

main()
