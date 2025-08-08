
document = {
    "Bubble Sort":"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break""",


    "Insertion Sort":"""
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
        arr[j+1]=x""",


    "Merge Sort":"""
def merge_sort_optimized(arr):
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
""",

"Selection Sort":"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first unsorted element
        min_index = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    """

}

description = {
    "Attributes" : ["Algorithm Type","Method","Time Complexity (Best)","Time Complexity (Average)","Time Complexity (Worst)","Space Complexity"],
    "Bubble Sort" : ["Comparison-based sorting","Repeatedly swaps adjacent elements if in wrong order","O(n)  (when the array is already sorted)","O(n²)","O(n²)","O(1) (in-place sorting)"],
    "Insertion Sort" : ["Comparison-based sorting","Inserts each element into its correct position in a sorted portion","O(n) (when the array is already sorted)","O(n²)","O(n²)","O(1) (in-place sorting)"],
    "Merge Sort" : ["Comparison-based sorting (Divide and Conquer)","Recursively divides array into halves, sorts, and merges sorted halves","O(n log n)","O(n log n)","O(n log n)","O(n) (requires additional space for merging)"],
    "Selection Sort" : ["Comparison based sorting (Unstable)", "Selection", "O(n²) - always performs comparisons even if already sorted", "O(n²) - compares all pairs in the worst case", "O(n²) - for reverse sorted or unsorted inputs", "O(1) - in-place sorting"]

}