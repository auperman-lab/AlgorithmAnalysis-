import time
import random

from matplotlib import pyplot as plt
from prettytable import PrettyTable


def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def heapify(arr, N, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < N and arr[largest] < arr[left]:
        largest = left

    if right < N and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
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


def heapsort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def icantbeliveitcansort(arr):
    for i in arr:
        for j in arr:
            if i < j:
                i, j = j, i


arr_list = []


lengths = [100, 500, 1000, 2000, 3000, 3500, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for length in lengths:
    arr = [random.randint(0, 10000) for _ in range(int(length))]
    arr_list.append(arr)


table = PrettyTable()


execution_func = {'heapsort': heapsort,
                  'quicksort': quicksort,
                  'mergesort': mergesort,
                  'icantbeliveitcansort': icantbeliveitcansort}

execution_times = {'heapsort': [],
                   'quicksort': [],
                   'mergesort': [],
                   'icantbeliveitcansort': []}

name = 'icantbeliveitcansort'

for arr in arr_list:
    _, execution_time = calculate_execution_time(execution_func[name], arr)
    execution_times[name].append(execution_time)

plt.plot([len(arr) for arr in arr_list], execution_times[name], label=name, marker='.')

plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of ' + name)
plt.legend()
plt.show()

table.field_names = ["Array length", "Execution Time (seconds)"]
for n, execution_time in zip([len(arr) for arr in arr_list], execution_times[name]):
    table.add_row([n, execution_time])

print(table)
