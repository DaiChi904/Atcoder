def main():
    N, L = map(int, input().split())
    d = list(map(int, input().split()))

    if L % 3 != 0:
        print(0)
        return
    
    amountOfEachPoints = [0] * L
    # this is fine 
    nextPointOffset: int = int(L / 3)

    idx = 0
    amountOfEachPoints[idx] += 1
    for i in range(N - 1):
        idx = (idx + (d[i])) % L
        amountOfEachPoints[idx] += 1
    
    res = 0

    for i in range(L):
        p1 = amountOfEachPoints[i]
        p2 = amountOfEachPoints[(i + nextPointOffset) % L]
        p3 = amountOfEachPoints[(i + (2 * nextPointOffset)) % L]

        res = p1 * p2 * p3 + res
    
    print(int(res / 3))


main()
