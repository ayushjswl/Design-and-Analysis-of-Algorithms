from decorators.decorators import timer, random_array



@random_array(1,999)
def sample_size(arr):
    return arr


@timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

@timer
def insertion_sort(arr):
    n = len(arr)
    if n<=1 :
        return
    for i in range(1, n):
        x = arr[i]
        j = i-1
        while  j>=0 and x<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=x
    return arr

@timer
def merge_sort(arr):
    def sort_helper(arr, temp, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        sort_helper(arr, temp, left, mid)
        sort_helper(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

    def merge(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]

    temp = [0] * len(arr)
    sort_helper(arr, temp, 0, len(arr) - 1)
    return arr

