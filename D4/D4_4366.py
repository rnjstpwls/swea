import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    binary = input()
    ternary = input()

    bin_candidate = []
    tern_candidate = []

    for i in range(len(binary)):
        tmp = str()
        for j in range(len(binary)):
            if i != j:
                tmp += binary[j]
            else:
                tmp += str(1 - int(binary[j]))
        bin_candidate.append(int(tmp,2))

    for i in range(len(ternary)):
        tmp = str()
        for j in range(len(ternary)):
            if i != j:
                tmp += ternary[j]
            else:
                tmp += str((int(ternary[j])+1)%3)
        tern_candidate.append(int(tmp,3))

        tmp = str()
        for j in range(len(ternary)):
            if i != j:
                tmp += ternary[j]
            else:
                tmp += str((int(ternary[j])+2)%3)
        tern_candidate.append(int(tmp, 3))

    result = set(bin_candidate) & set(tern_candidate)

    print(f'#{tc}',list(result)[0])
