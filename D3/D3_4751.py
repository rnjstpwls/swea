import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    text = input()
    length = len(text)

    # + .
    first_decoration = '..#.'
    # + .
    second_decoration = '.#.#'

    for i in range(length):
        print(first_decoration,end='')
    print('.')

    for i in range(length):
        print(second_decoration,end='')
    print('.')

    for i in range(length):
        print('#.'+text[i]+'.',end='')
    print('#')

    for i in range(length):
        print(second_decoration, end='')
    print('.')

    for i in range(length):
        print(first_decoration,end='')
    print('.')