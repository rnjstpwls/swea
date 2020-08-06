import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    bus_route = []
    for i in range(N):
        bus_route += [list(map(int,input().split()))]
    # print(bus_route)

    P = int(input())

    bus_station = []

    for i in range(P):
        bus_station.append(int(input()))
    # print(bus_station)

    result = []
    for i in bus_station:
        cnt = 0
        for j in range(N):
            if bus_route[j][0] <= i <= bus_route[j][1]:
                cnt += 1
        result.append(cnt)

    # print(result)

    print(f'#{test_case}',end=' ')
    for i in result:
        print(i,end=' ')
    print()
