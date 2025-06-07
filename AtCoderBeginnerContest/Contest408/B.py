def main():
    N = int(input())
    A = list(map(int, input().split()))

    Aset = set(A)
    res = list(Aset)
    res.sort()


    print(len(res))
    res=[str(a) for a in res]
    res=" ".join(res)
    print(res)

main()
