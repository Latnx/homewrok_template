num = 0


def merge(arr, l, m, r):
    C = [0] * len(arr)
    start1, start2 = l, m + 1
    index = 0
    global num
    while start1 <= m and start2 <= r:
        if arr[start1] < arr[start2]:
            C[index] = arr[start1]
            start1 += 1
        else:
            C[index] = arr[start2]
            start2 += 1
        index += 1
        num += 1
    if start1 <= m:
        C[index:m - start1 + index + 1] = arr[start1:m + 1]
    else:
        C[index:r - start2 + index + 1] = arr[start2:r + 1]
    arr[l:r + 1] = C[0: r + 1 - l]


def mergeSort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    global num
    temp = num
    num = 0
    return temp


# arr = [12, 11, 13, 5, 6, 7, 9, 30, 7, 6, 413, 5, 2, 7, 8, 5]
#
# print(mergeSort(arr, 0, len(arr) - 1))
#
# print(arr)
