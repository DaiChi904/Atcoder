def main():
    N = int(input())
    A = list(map(int, input().split()))

    results: list[int] = []

    for i in range(N):
        try:
            length = A.index(A[i], i + 1) + 1
            results.append(length)
        except:
            None
        
    sortedResults: list[int] = sorted(results, reverse=True)

    print(sortedResults[0] if len(sortedResults) > 0 else -1)

main()
