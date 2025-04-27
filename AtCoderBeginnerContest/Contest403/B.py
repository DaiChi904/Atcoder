# なんで動かないんですかね。。。

def main():
    T = str(input())
    U = str(input())

    isContain = False

    for i in range(len(T)):
        if (isContains(T, U, i)):
            isContain = True
            break

    print("Yes" if isContain else "No")

def isContains(T: str, U: str, TstartIndex: int) -> bool:
    currentUIndex = 0
    isContain = True

    for i in range(TstartIndex, len(T)):
        if T[i] == U[currentUIndex] or T[i] == "?":
            currentUIndex += 1
        else:
            isContain = False
            break
        
    return isContain

main()