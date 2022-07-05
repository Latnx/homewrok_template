

class QuickSort:
    n = 0

    def partition(self, arr, low, high):
        i = low + 1
        j = high
        x = arr[low]
        while i < j:
            while arr[i] <= x and i < high:
                i += 1
                self.n += 1
            while arr[j] >= x and j > low:
                j -= 1
                self.n += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]

        return i

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
        return self.n
