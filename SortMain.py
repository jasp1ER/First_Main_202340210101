import copy

def zcQuickSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()
    
    # 内部递归函数，实现快速排序逻辑
    def quickSortHelper(arr, low, high):
        # 递归终止条件：当子数组长度为1或0时停止
        if low < high:
            # 获取分区点索引（基准元素最终位置）
            pivotIndex = partition(arr, low, high)
            # 递归排序左子数组（小于基准的部分）
            quickSortHelper(arr, low, pivotIndex - 1)
            # 递归排序右子数组（大于基准的部分）
            quickSortHelper(arr, pivotIndex + 1, high)
    
    # 分区函数：选择基准元素，将数组分为两部分
    # 参数: arr - 数组, low - 起始索引, high - 结束索引
    # 返回值: pivotIndex - 基准元素的最终位置索引
    def partition(arr, low, high):
        # 选择最右侧元素作为基准
        pivot = arr[high]
        # i指向小于基准的区域的下一个位置
        i = low - 1
        
        # 遍历当前分区，将小于基准的元素移到左侧
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                # 交换元素，扩大小于基准的区域
                arr[i], arr[j] = arr[j], arr[i]
        
        # 将基准元素放到正确位置（i+1处）
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # 执行快速排序
    n = len(sortedArr)
    if n > 1:
        quickSortHelper(sortedArr, 0, n - 1)
    
    return sortedArr


def zwySelectionSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()
    n = len(sortedArr)

    # 外层循环：确定每一轮放置最小值的位置
    for i in range(n - 1):
        minIndex = i

        # 内层循环：寻找最小值下标
        for j in range(i + 1, n):
            if sortedArr[j] < sortedArr[minIndex]:
                minIndex = j

        # 交换：将最小值放到当前i位置
        sortedArr[i], sortedArr[minIndex] = sortedArr[minIndex], sortedArr[i]

    return sortedArr


def fzhInsertionSort(arr):
    """
    插入排序算法
    核心思想：将数组分为已排序区和未排序区，逐个将未排序元素插入到已排序区的正确位置
    """
    # 创建数组副本，避免修改原数组
    sortedArr = arr.copy()
    n = len(sortedArr)
    
    # 从第2个元素开始遍历（第1个元素视为已排序区）
    for i in range(1, n):
        # 当前要插入的元素（未排序区的第一个元素）
        current = sortedArr[i]
        
        # 已排序区的最后一个位置
        j = i - 1
        
        # 在已排序区从后向前查找插入位置
        # 如果已排序元素大于当前元素，则将其后移，腾出插入位置
        while j >= 0 and sortedArr[j] > current:
            sortedArr[j + 1] = sortedArr[j]  # 元素后移一位
            j -= 1  # 继续向前比较
        
        # 找到正确位置，插入当前元素
        sortedArr[j + 1] = current
        
        # 可选：打印每轮排序过程，便于理解算法执行
        # print(f"第{i}轮排序后：{result}")
    
    return sortedArr


def xwBubbleSort(arr):
    """
    冒泡排序算法实现
    算法思想：重复遍历数组，比较相邻元素，将较大的元素向后移动
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    # 复制原数组，避免修改原数据
    sortedArr = copy.deepcopy(arr)
    n = len(sortedArr)
    
    # 外层循环：控制排序轮数
    for i in range(n - 1):
        # 优化标志：如果本轮没有发生交换，说明数组已经有序
        swapped = False
        
        # 内层循环：控制每轮比较次数
        for j in range(n - 1 - i):
            # 如果当前元素大于下一个元素，则交换
            if sortedArr[j] > sortedArr[j + 1]:
                sortedArr[j], sortedArr[j + 1] = sortedArr[j + 1], sortedArr[j]
                swapped = True
        
        # 如果没有发生交换，提前结束排序
        if not swapped:
            break
    
    return sortedArr


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
    # 测试数组: 统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组: ", testArr)
    
    # 成员调用自己的算法: 后续在此处添加代码
    # 调用快速排序算法
    result = zcQuickSort(testArr)
    print("zc-快速排序算法排序结果: ", result)
    
    # 调用选择排序算法
    sortedArr = zwySelectionSort(testArr)
    print("zwy-选择排序算法排序结果: ", sortedArr)
    
    # 调用插入排序算法
    sortedArr = fzhInsertionSort(testArr)
    print("fzh-插入排序算法排序结果: ", sortedArr)
    
    # 调用冒泡排序算法
    sortedArr = xwBubbleSort(testArr)
    print("xw-冒泡排序算法排序结果: ", sortedArr)
    
    # 调用归并排序算法
    sortedArr = hjhMergeSort(testArr)
    print("hjh-归并排序算法排序结果: ", sortedArr)
    
    # 验证排序正确性
    print("验证（Python内置排序）：", sorted(testArr))