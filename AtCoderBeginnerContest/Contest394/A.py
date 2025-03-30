Str = input()

for i in range(10):
    if i != 2:
        Str = Str.replace(str(i), "")

print(Str)
