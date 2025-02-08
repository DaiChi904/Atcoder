s = input().split()

D = s[0]

if D == "N":
    print("S")
elif D == "E":
    print("W")
elif D == "W":
    print("E")
elif D == "S":
    print("N")
elif D == "NE":
    print("SW")
elif D == "NW":
    print("SE")
elif D == "SW":
    print("NE")
elif D == "SE":
    print("NW")
