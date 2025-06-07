def main():
    N = int(input())
    P = list(map(int, input().split()))

    res = get_tildes(P)

    print(res)

def get_tildes(P: list[int]) -> int:
    tildes = 0

    if len(P) < 4:
        return tildes
    
    for i in range(len(P)):
        if i < 4:
            continue

        for j in range(0, len(P) - i):
            condition_1 = 0
            condition_2 = 0
            for k in range(j, j + i):
                if P[k - 1] < P[k] and P[k - 1] > P[k]:
                    condition_1 += 1
                if P[k - 1] > P[k] and P[k - 1] < P[k]:
                    condition_2 += 1

                print(i, j, k, condition_1, condition_2)
                    

            if condition_1 == 1 and condition_2 == 1:
                tildes += 1
        
    return tildes


main()
