def main():
    N = int(input())
    
    square = [["#" for i in range(N)] for j in range(N)]

    for i in range(N):
        if i == 0:
            continue
        
        j = N + 1 - i
        if i <= j:
            if i % 2 == 1:
                for k in range(i - 1, j):
                    for s in range(i - 1, j):
                        square[k][s] = "#"
            else:
                for k in range(i - 1, j):
                    for s in range(i - 1, j):
                        square[k][s] = "."

    for i in range(N):
        for j in range(N):
            print(square[i][j], end="")
        print()

main()
