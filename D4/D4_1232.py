import sys
sys.stdin = open('input.txt','r')

def is_number(num):
    if num in operator:
        return False
    else:
        return True


def calculate(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2

def post_order(idx):
    if idx > N:
        return
    if tree[idx] in operator:
        post_order(int(operator_list[idx][0]))
        post_order(int(operator_list[idx][1]))
    equation.append(tree[idx])

operator = ['+', '-', '*', '/']

for tc in range(1,11):
    N = int(input())
    tree = [0] * (N+1)
    operator_list = [[0]*2 for _ in range(N+1)]
    for _ in range(N):
        a, b, *c = input().split()
        tree[int(a)] = b
        if b in operator:
            operator_list[int(a)] = c
    equation = []
    post_order(1)
    calculator = []

    calculator.append(equation.pop(0))
    calculator.append(equation.pop(0))

    while equation:
        tmp = equation.pop(0)
        if is_number(tmp):
            calculator.append(tmp)
            continue
        else:
            num1 = int(calculator.pop())
            num2 = int(calculator.pop())
            calculator.append(calculate(tmp,num2,num1))
    print(f'#{tc}', int(calculator.pop()))