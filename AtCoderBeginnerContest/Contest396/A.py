def main():
    N = int(input())
    A = list(map(int, input().split()))

    isConsecutive = False

    for i in range(N):
        first = i - 2
        second = i - 1
        third = i

        if A[first] == A[second] and A[first] == A[third] and A[second] == A[third]:
            isConsecutive = True
            break

    print("Yes" if isConsecutive else "No")

main()
