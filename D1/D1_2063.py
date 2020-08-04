import sys
sys.stdin = open('input.txt', 'r')

num = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[num//2])

