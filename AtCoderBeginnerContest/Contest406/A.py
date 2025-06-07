def main():
    A, B, C, D = map(int, input().split())

    is_expired = False

    deadline = get_minutes(A, B)
    hand_in = get_minutes(C, D)

    if deadline < hand_in:
        is_expired = True

    print("No" if is_expired else "Yes")

def get_minutes(h, m):
    return h * 60 + m

main()
