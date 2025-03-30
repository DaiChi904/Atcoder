def abs(a):
    return a if a >= 0 else -a


def main():
    N, M = map(int, input().split())
    B = list(map(int, input().split()))
    W = list(map(int, input().split()))

    numOfBlack = 0
    numbOfWhite = 0
    selected = list()

    B.sort(reverse=True)
    W.sort(reverse=True)

    changed = False
    for _ in range(N if N > M else M):
        if numOfBlack < N:
            if B[numOfBlack] >= 0:
                selected.append(B[numOfBlack])
                numOfBlack += 1
                changed = True
        
        if numbOfWhite < M:
            if numOfBlack > numbOfWhite and W[numbOfWhite] >= 0:
                selected.append(W[numbOfWhite])
                numbOfWhite += 1
                changed = True

        if numbOfWhite < M and numOfBlack < N:
            if numOfBlack >= numbOfWhite and abs(B[numOfBlack]) <= abs(W[numbOfWhite]) and W[numbOfWhite] >= 0:
                selected.append(B[numOfBlack])
                selected.append(W[numbOfWhite])
                if numOfBlack < N:
                    numOfBlack += 1
                numbOfWhite += 1
                changed = True

        if not changed:
            break

    print(sum(selected))

main()
