import sys
sys.stdin = open('input.txt','r')



T = int(input())

for tc in range(1,T+1):
    namefile = [[] for _ in range(51)]
    N = int(input())
    for _ in range(N):
        name = input()
        namefile[len(name)].append(name)
    result=  []
    for i in namefile:
        if i:
            result += sorted(list(set(i)))

    print('#%d' %tc)
    for i in result:
        print(i)