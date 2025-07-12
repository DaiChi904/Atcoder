def main():
    N, L , R= map(int, input().split())
    XY = [list(map(int, input().split())) for l in range(N)]

    res = 0

    for xy in XY:
        x = xy[0]
        y = xy[1]

        if (L >= x and R <= y):
            res += 1

    print(res)

main()
