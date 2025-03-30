def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = []

    for i in range(N):
        duplicated = 0
        forward = A[:i]
        backward = A[i:]

        forward.sort()
        backward.sort()

        for j in range(i):
            if j == 0:
                continue
            s = forward[j - 1]
            t = forward[j]
            if s == t:
                duplicated += 1

        for j in range(N - i):
            if j == 0:
                continue
            s = backward[j - 1]
            t = backward[j]
            if s == t:
                duplicated += 1

        result.append(len(forward) + len(backward) - duplicated)
        
    print(max(result))

main()
