def main():
    N, S = map(int, input().split())
    T = list(map(int, input().split()))

    timeout = S + 0.5

    is_awakeing = True

    for i in range(N):
        if i == 0:
            if T[i] >= timeout:
                is_awakeing = False
                break
        if T[i] - T[i - 1] >= timeout:
            is_awakeing = False
            break

    print("Yes" if is_awakeing else "No")

main()
