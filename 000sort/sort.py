#encoding=utf-8
''' python sort '''

def insert_sort(lists):
    ''' 插入排序'''
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i -1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def shell_sort(lists):
    ''' 希尔排序'''
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

def bubble_sort(lists):
    '''冒泡排序'''
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

def quick_sort(lists, left, right):
    '''快速排序'''
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    print lists
    print left, right
    print low, high
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

def select_sort(lists):
    '''选择排序'''
    count = len(lists)
    for i in range(0, count):
        min_ = i
        for j in range(i + 1, count):
            if lists[min_] > lists[j]:
                min_ = j
        lists[min_], lists[i] = lists[i], lists[min_]
    return lists

def merge(left, right):
    '''合并'''
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print left, right, result
    return result

def merge_sort(lists):
    '''归并排序'''
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


LISTS = [3, 5, 1, 7, 2, 11, 89, 34]
#print insert_sort(LISTS)
#print shell_sort(LISTS)
#print bubble_sort(LISTS)
print LISTS
#print quick_sort(LISTS, 0, 7)
#print select_sort(LISTS)
print merge_sort(LISTS)
