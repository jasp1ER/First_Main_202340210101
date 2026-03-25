def hjhMergeSort(arr):
    """
    归并排序（Merge Sort）
    :param arr: 待排序列表
    :return: 排序后的新列表
    """
    if len(arr) <= 1:
        return arr

    # 分割数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 递归排序
    left_sorted = hjhMergeSort(left_half)
    right_sorted = hjhMergeSort(right_half)

    # 合并两个有序数组
    return hjhMerge(left_sorted, right_sorted)


def hjhMerge(left, right):
    """
    合并两个有序数组
    :param left: 左侧有序列表
    :param right: 右侧有序列表
    :return: 合并后的有序列表
    """
    merged = []
    i = j = 0

    # 比较两个数组元素，按顺序放入 merged
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 处理剩余元素
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    sortedArr = hjhMergeSort(testArr)
    print("排序后数组：",sortedArr)

