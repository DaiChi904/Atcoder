def main():
    N = int(input())
    T = str(input())
    A = str(input())

    isOk = False

    for i in range(N):
        if T[i] == A[i] == "o":
            isOk = True
            break

    print("Yes" if isOk else "No")

main()
