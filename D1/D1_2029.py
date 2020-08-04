T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    div = a // b
    mod = a % b
    print('#%d' %test_case, div, mod)