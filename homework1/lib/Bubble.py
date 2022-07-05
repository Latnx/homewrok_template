def Bubble(list, n):
    num = 0
    for i in range(n-1):
        for j in range(n - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                num += 1
    return num



