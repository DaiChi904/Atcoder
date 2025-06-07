def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(N + 1):
        temp = 0
        for j in range(N):
            if A[j] >= i:
                temp += 1
        if temp < i:
            break
        res = i
        
    
    print(res)

main()
