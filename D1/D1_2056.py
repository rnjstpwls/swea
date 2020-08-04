import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    txt = input()
    year = txt[0:4]
    month = txt[4:6]
    day = txt[6:8]
    month_num = int(month)
    day_num = int(day)

    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]

    print('#%d ' % test_case, end='')

    if month_num in day31:
        if day_num > 31 or day_num < 1:
            print('-1')
        else:
            print(year+'/'+month+'/'+day)
    elif month_num in day30:
        if day_num > 30 or day_num < 1:
            print('-1')
        else:
            print(year+'/'+month+'/'+day)
    elif month_num == 2:
        if day_num > 28 or day_num < 1:
            print('-1')
        else:
            print(year+'/'+month+'/'+day)
    else:
        print('-1')
