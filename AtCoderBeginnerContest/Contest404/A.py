def main():
    S = str(input())

    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    for s in S:
        if s in alphabets:
            alphabets.remove(s)

    print(alphabets[0])


main()
