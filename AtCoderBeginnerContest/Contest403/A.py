def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = 0

    for i in range(N):
        if isOdd(i +  1):
            res += A[i]

    print(res)
    

def isOdd(num):
    return num % 2

main()
