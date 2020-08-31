import sys
sys.stdin = open('input.txt','r')

def is_number(char):
    if ord('0') <= ord(char) <= ord('9'):
        return True
    else:
        return False

def icp(char): # in-coming priority
    if char == '*':
        return 2
    if char == '+':
        return 1
    if char == '(':
        return 3


def isp(char): # in-stack priorty
    if char == '*':
        return 2
    if char == '+':
        return 1
    if char == '(':
        return 0


def operator(char, stack):
    if char == '+':
        return stack.pop() + stack.pop()
    elif char == '*':
        return stack.pop() * stack.pop()

for tc in range(1,11):
    length = int(input())
    equation = input()
    stack = []
    result = []

    for char in equation:
        if is_number(char):
            result.append(char)
            continue
        if char == ')':
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    break
                result.append(tmp)
            continue

        if not(stack):
            stack.append(char)
            continue

        if isp(stack[-1]) < icp(char):
            stack.append(char)
        else:
            while True:
                if stack and isp(stack[-1]) >= icp(char):
                    result.append(stack.pop())
                else:
                    stack.append(char)
                    break
    while stack:
        result.append(stack.pop())

    for char in result:
        if is_number(char):
            stack.append(int(char))
        else:
            stack.append(operator(char, stack))

    print(f'#{tc}', stack[-1])

