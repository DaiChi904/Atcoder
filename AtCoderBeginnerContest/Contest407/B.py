def main():
    X, Y = map(int, input().split())

    cases: list[list[int]] = []
    for i in range(1, 7):
        for j in range(1, 7):
            comb = [i, j]
            cases.append(comb)

    res = checkCondition(X, Y, cases)

    print(len(res) / 36)

def checkCondition(X: int, Y: int, cases: list[int]) -> list[int]:
    res = list(filter(lambda x: sum(x) >= X or abs(x[0] - x[1]) >= Y, cases))

    return res

main()

