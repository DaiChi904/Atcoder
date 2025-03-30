def main():
    S = str(input())
    while S.find("WA") != -1:
        S = S.replace("WA", "AC", 1)

    print(S)

main()
