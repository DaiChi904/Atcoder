def main():
    S = str(input())

    S = list(S)

    res: list[str] = []
    cnt = 0

    for i in range(len(S)):
        res = useA(res)
        while S[i] != res[i]:
            useB(res)
            cnt += 1

    print(cnt)
    print(res)


def useA(res: str):
    res += "0"

    return res

def useB(res: str):
    for i in range(len(res)):
        rs = res[i]
        if rs != "9":
            res[i] = str(int(rs) + 1)
        else:
            res[i] = "0"

    return res

main()
