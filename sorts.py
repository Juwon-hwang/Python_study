def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
            

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        
        
def heap_sort(data):
    for i in range(1, len(data)):
        c = i
        while c != 0:
            r = (c - 1) // 2
            if data[r] < data[c]:
                data[r], data[c] = data[c], data[r]
                
            c = r
    
    for i in range(len(data) - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        r = 0
        c = 1
        while c < i:
            c = 2 * r + 1
            if(c < i - 1) and (data[c] < data[c + 1]):
                c += 1
            if(c < i) and (data[r] < data[c]):
                data[r], data[c] = data[c], data[r]
            r = c
            
            
def merge_sort(data):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        
        while l < mid and h < high:
            if data[l] < data[h]:
                temp.append(data[l])
                l += 1
            else:
                temp.append(data[h])
                h += 1
                
        while l < mid:
            temp.append(data[l])
            l += 1
        while h < high:
            temp.append(data[h])
            h += 1
            
        for i in range(low, high):
            data[i] = temp[i - low]
            
    return sort(0, len(data))


def quick_sort(data, start, end):
    if start >= end:
        return
    
    pivot = data[start]
    low = start + 1
    high = end
    
    while True:
        while low <= high and data[high] >= pivot:
            high = high - 1
            
        while low <= high and data[low] <= pivot:
            low = low + 1
            
        if low <= high:
            data[low], data[high] = data[high], data[low]
            
        else:
            break
        
    data[start], data[high] = data[high], data[start]
    
    quick_sort(data, start, high - 1)
    quick_sort(data, high + 1, end)
    
    
def python_sort(data):
    data.sort()
    
    
if __name__ == '__main__':
    import numpy as np
    import time
    import copy
    
    
    def measure(d, f):
        datas = copy.deepcopy(d)
        if f == quick_sort:
            l = len(datas)
            start = time.time()
            f(datas, 0, l - 1)
            end = time.time()
            
        else:
            start = time.time()
            f(datas)
            end = time.time()
            
        return (end - start) * 1000
    
    
    test1 = np.loadtxt('./dataset/test1.dat', delimiter=',', dtype=np.int64)
    test2 = np.loadtxt('./dataset/test2.dat', delimiter=',', dtype=np.int64)
    test3 = np.loadtxt('./dataset/test3.dat', delimiter=',', dtype=np.int64)        
    test4 = np.loadtxt('./dataset/test4.dat', delimiter=',', dtype=np.int64)
    test5 = np.loadtxt('./dataset/test5.dat', delimiter=',', dtype=np.int64)

    
    f_list = [selection_sort, heap_sort, insertion_sort, quick_sort, merge_sort, python_sort]
    data_list = [test1, test2, test3, test4, test5]
    row = ['selection', 'heap', 'insertion', 'quick', 'merge', 'python']
    col = ['', '500', '1K', '5K', '10K', '100K']
    
    
    result = [[] for _ in range(6)]
    for i in range(6):
        for data in data_list:
            result[i].append(measure(data, f_list[i]))
            
    for s in col:
        print(s.rjust(15), end='')
    print()
    
    for i in range(6):
        print(row[i].rjust(15), end='')
        for t in result[i]:
            print(f'{t:.3f}ms'.rjust(15), end='')
        print()
