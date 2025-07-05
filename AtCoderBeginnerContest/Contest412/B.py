def main():
    S = str(input())
    T = str(input())

    inclued: list[str] = []

    for i in range(len(S)):
        if (S[i].isupper() and i != 0):
            inclued.append(S[i - 1])

    for i in range(len(T)):
        if (T[i] in inclued):
            inclued.remove(T[i])

    print("Yes" if len(inclued) == 0 else "No")

main()
