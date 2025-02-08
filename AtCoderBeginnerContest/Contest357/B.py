letters = input()
letters_list = list(letters)

upper_cnt = 0
lower_cnt = 0

for i in range(0, len(letters_list), 1):
    if letters_list[i].isupper() == True:
        upper_cnt += 1
    else:
        lower_cnt += 1
if upper_cnt < lower_cnt:
    print(letters.lower())
else:
    print(letters.upper())
