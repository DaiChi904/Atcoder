def main():
    N = int(input())
    P = list(map(int, input().split()))
    
    r = 1

    rank_result = [0 for _ in range(N)]

    while 0 in rank_result:
        k = 0
        x = max(P)
        for j in range(N):
            if P[j] == x:
                k += 1
                P[j] = 0
                rank_result[j] = r

        r += k

    for rank in rank_result:
        print(rank)

main()
