for test_case in range(1,11):

    dump = int(input())
    boxes = list(map(int,input().split()))
    # print(dump)
    # print(boxes)
    while dump > 0:
        tmp_max = max(boxes)
        tmp_min = min(boxes)
        boxes[boxes.index(tmp_max)] -= 1
        boxes[boxes.index(tmp_min)] += 1
        dump -= 1

    print('#%d' %test_case, max(boxes)-min(boxes))