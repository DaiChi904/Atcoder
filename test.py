n = list(map(int, input().split()))

l1 = []
l2 = []

for i in range (1, n[0] + 1 , 1):  
    l1.append(i)

for i in range (n[1], n[2] + 1, 1):
    l2.append(i)

l2.reverse()

l1[n[1]-1:n[2]] = l2

print(*l1)
