import numpy as np
import time
import copy

def insertion_sort(data):
    #TODO: Implement insertion sort algorithm
    for end in range(1, len(data)):
        for i in range(end, 0, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]

def selection_sort(data):
    #TODO: Implement selection sort algorithm
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def heap_sort(data):
    #TODO: Implement heap sort algorithm
    n = len(data)
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (data[r] < data[c]):
                data[r], data[c] = data[c], data[r]
            c = r
    for j in range(n-1, -1, -1):
        data[0] , data[j] = data[j], data[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            if (c<j-1) and (data[c] < data[c+1]):
                c += 1
            if (c<j) and (data[r] < data[c]):
                data[r], data[c] = data[c], data[r]
            r=c

def merge_sort(data):
    #TODO: Implement merge sort algorithm
    if len(data) > 1:

        r = len(data)//2
        L = data[:r]
        M = data[r:]

        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            data[k] = M[j]
            j += 1
            k += 1

def quick_sort(data):
    #TODO: Implement quick sort algorithm
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = data[(low + high) // 2]
        while low <= high:
            while data[low] < pivot:
                low += 1
            while data[high] > pivot:
                high -= 1
            if low <= high:
                data[low], data[high] = data[high], data[low]
                low, high = low + 1, high - 1
        return low
    return sort(0, len(data) - 1)

def built_in_sort(data):
    #TODO: Use python built-in sort function
    data.sort()


functions = [selection_sort, heap_sort, insertion_sort, quick_sort, merge_sort, built_in_sort]
fuc_names = {selection_sort: 'selection', heap_sort: 'heap', insertion_sort: 'insertion', quick_sort: 'quick', merge_sort: 'merge', built_in_sort: 'python'}
data_files = ['test1.dat', 'test2.dat', 'test3.dat', 'test4.dat', 'test5.dat']
dataset = []
std = np.array([0])
std.astype('datetime64[ms]')

for f in data_files:
    data_file = open("'./dataset/test.dat/{0}".format(f), 'r')
    data = data_file.readlines()
    dataset.append(data)
    data_file.close()

col = ['', '500', '1K', '5K', '10K', '100K']
for s in col:
    print(s.rjust(15), end='')
print()

for f in functions:
    time_list = []
    for data in dataset:
        datas = copy.deepcopy(data)
        start = time.time()
        f(datas)
        end = time.time()
        time_list.append(round((end - start)*1000, 2))

    t_arr = np.array(time_list)
    t_arr.astype('datetime64[ms]')
    t_arr = t_arr - std[0]
    print(fuc_names[f].rjust(15), end='')
    for i in t_arr:
        print(f'{i}ms'.rjust(15), end='')
    print()