s = input().split()

isOk = False

for i in range(3):
    for j in range(3):
        for k in range(3):
            if int(s[i]) * int(s[j]) == int(s[k]) and not (i == k or i == j or j == k):
                isOk = True

if isOk:
    print("Yes")
else:
    print("No")
