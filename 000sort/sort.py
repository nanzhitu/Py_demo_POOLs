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
                    if Lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


Lists = [3, 5, 1, 7, 3, 11, 89, 34]
#print insert_sort(Lists)
print shell_sort(Lists)
