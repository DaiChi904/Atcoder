def main():
    N = int(input())
    cl = []
    for i in range(N):
        c,l=input().split()
        cl.append([c, int(l)])

    res = ""
    cnt = 0

    for CL in cl:
        c = CL[0]
        l = CL[1]

        cnt += l

        if (cnt > 100):
            break

        res += c * l

    print(res if cnt <= 100 else "Too Long")

main()
