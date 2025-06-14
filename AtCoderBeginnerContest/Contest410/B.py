def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    boxes: list[int] = [0] * N
    res: list[int] = []

    for q in X:
        if q == 0:
            minimum: int = min(boxes)
            minIdx: int = boxes.index(minimum)
            boxes[minIdx] += 1

            res.append(minIdx + 1)
        else:
            boxes[q - 1] += 1

            res.append(q)

    res = [str(a) for a in res]
    print(" ".join(res))

main()
