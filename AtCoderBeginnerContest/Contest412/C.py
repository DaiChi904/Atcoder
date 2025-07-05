def main():
    N = int(input())
    queries = [list(map(int, input().split())) for _ in range(N * 2)]

    for i in range(N):
        amt = 2
        length = queries[i * 2][0]
        dominoes = list(queries[(i * 2) + 1])

        first = dominoes.pop(0)
        last = dominoes.pop()

        dominoes.sort()

        if (last <= (first * 2)):
            print(amt)
            continue

        if (length == 2):
            print(-1)
            continue

        prev = first
        for j in range(length - 2):
            curr = dominoes[j]
            next = last if j == (length - 3) else dominoes[j + 1]
            if (curr <= (prev * 2) and next > (prev * 2)):
                amt += 1
                prev = curr
            
            if (length - 3 == j and last > (prev * 2) and last > (curr * 2)):
                print(-1)
                continue

        print(amt)

main()
