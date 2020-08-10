import sys
sys.stdin = open('input.txt','r')

T = int(input())
vowels = ['a','e','i','o','u']
for test_case in range(1,T+1):
    text = input()
    result = str()
    for i in text:
        if i in vowels:
            continue
        result += i
    print(f'#{test_case} {result}')
