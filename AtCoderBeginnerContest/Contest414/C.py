# 無理
def main():
    A = int(input())
    N = int(input())

    res = 0

    for i in range(1, N + 1):
        nomal = i
        nArySystem = int(i, A)

        if (isPalindromeNumber(nomal) and isPalindromeNumber(nArySystem) and i != A):
            print(nomal)
            res += nomal

    print(res)
            

def isPalindromeNumber(number: int):
    strNumber = str(number)
    for i in range(len(strNumber)):
        if (strNumber[i] != strNumber[len(strNumber) - 1 - i]):
            return False
    return True

def calcNArySystemValue(number: int, A: int):
    temp = number
    res = ""
    while (True):
        rem = temp % A
        temp = temp // A
        res += str(rem)

        if (temp == 0):
            break

    return int(res)

main()
