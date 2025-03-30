def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    isOk = True

    for i in range(N):
        if i == 0:
            continue
        if A[i] > A[i - 1]:
            continue
        else:
            isOk = False
            break

    print("Yes" if isOk else "No")

main()
