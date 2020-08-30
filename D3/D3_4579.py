import sys
sys.stdin = open('input.txt','r')

def pelindrome(txt):
    if len(txt) <= 1 or txt[0] == '*' or txt[-1] == '*':
        return 'Exist'
    if txt[0] == txt[-1]:
        return pelindrome(txt[1:-1])
    else:
        return 'Not exist'

T = int(input())

for tc in range(1,T+1):
    txt = input()

    print(f'#{tc}', pelindrome(txt))