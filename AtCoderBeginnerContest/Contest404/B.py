def main():
    N, M = map(int, input().split())
    eadges = [list(map(int, input().split())) for _ in range(M)]

    baseVertexs = [0 for _ in range(0, N + 1)]
    distinationVertices = [0 for _ in range(0, N + 1)]

    isCycledGraph = True

    if abs(N - M) != 0:
        isCycledGraph = False

    for eadge in eadges:
        baseVertexs[eadge[0]] += 1
        distinationVertices[eadge[1]] += 1

    for i in range(1, N + 1):
        if i == 0:
            continue
        if (baseVertexs[i] > 2 or distinationVertices[i] > 2) or (baseVertexs[i] < 1 and distinationVertices[i] < 1):
            isCycledGraph = False
            break

    print("Yes" if isCycledGraph else "No")

main()
