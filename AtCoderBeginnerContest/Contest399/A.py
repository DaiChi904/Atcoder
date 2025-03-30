def main():
    N = int(input())
    S = str(input())
    T = str(input())

    haming_distance = 0

    for i in range(N):
        if S[i] != T[i]:
            haming_distance += 1

    print(haming_distance)

main()
