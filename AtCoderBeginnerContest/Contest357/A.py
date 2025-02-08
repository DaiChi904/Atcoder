# N = 人数, M = 消毒可能な手の本数

n = list(map(int, input().split()))
alien = list(map(int, input().split()))

last = n[1]
cnt = int(0)

for i in range(0, n[0], 1):
    last -= alien[i]
    if last >= 0:
        cnt += 1
    else:
        break

print(cnt)
