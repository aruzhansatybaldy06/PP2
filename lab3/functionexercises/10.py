list_1 = list(map(int, input().split()))

def set_1(list_1):
    list_2 = []
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    return list_2 

print(*set_1(list_1))
