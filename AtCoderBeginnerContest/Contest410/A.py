def main():
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    count = 0

    for r in A:
        if r >= K:
            count += 1

    print(count)

main()
