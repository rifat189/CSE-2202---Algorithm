import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def counting_sort(arr):
    max_val = int(max(arr))
    min_val = int(min(arr))
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def merge(arr, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        merge(arr, L, R)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def hybrid_sort(arr, threshold):
    if len(arr) <= threshold:
        insertion_sort(arr)  
    else:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        hybrid_sort(L, threshold)
        hybrid_sort(R, threshold)
        
        merge(arr, L, R)


def hybrid_sort_using_bubble_sort(arr, threshold):
    if len(arr) <= threshold:
        bubble_sort(arr)
    else:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        hybrid_sort(L, threshold)
        hybrid_sort(R, threshold)

        merge(arr, L, R)

def generate_random_data(n):
    return [random.randint(0, 100000) for _ in range(n)]



def measure_sorting_time(sorting_func, arr, *args):
    start_time = time.time()
    sorting_func(arr, *args)  
    end_time = time.time()
    return end_time - start_time


def main():
    n = int(input("Enter the size of random data (n): "))
    threshold = int(input("Enter the threshold for hybrid sort: "))

    data = generate_random_data(n)

    print("\nSorting with Insertion Sort...")
    data_insertion = data[:]
    insertion_time = measure_sorting_time(insertion_sort, data_insertion)
    print(f"Insertion Sort took {insertion_time:.6f} seconds.")

    print("\nSorting with Counting Sort...")
    data_counting = data[:]
    counting_time = measure_sorting_time(counting_sort, data_counting)
    print(f"Counting Sort took {counting_time:.6f} seconds.")

    print("\nSorting with Merge Sort...")
    data_merge = data[:]
    merge_time = measure_sorting_time(merge_sort, data_merge)
    print(f"Merge Sort took {merge_time:.6f} seconds.")

    print("\nSorting with Bubble Sort...")
    data_bubble = data[:]
    bubble_time = measure_sorting_time(bubble_sort, data_bubble)
    print(f"Bubble Sort took {bubble_time:.6f} seconds.")

    print("\nSorting with Hybrid Sort (Merge + Insertion)...")
    data_hybrid = data[:]
    hybrid_time = measure_sorting_time(hybrid_sort, data_hybrid, threshold)
    print(f"Insertion + merge sort {hybrid_time:.6f} seconds")


    print("\nSorting with Hybrid Sort (Bubble + Merge)...")
    data_bubble_merge = data[:]
    hybrid_time_using_bubble = measure_sorting_time(hybrid_sort_using_bubble_sort, data_bubble_merge, threshold)
    print(f"Bubble + merge sort {hybrid_time_using_bubble:.6f} seconds")

if __name__ == '__main__':
    main()
