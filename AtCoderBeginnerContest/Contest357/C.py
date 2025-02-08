level = int(input())
Si = ""

for row in range(0, 3**level, 1):
    for col in range(0, 3**level, 1):
        if (3*level <= col) and (3*level + 3*level >= col):
            Si = Si + "."
        else:
            Si = Si + "#"
        if col == 3**level - 1:
            Si = Si + "\n"

print(Si)

