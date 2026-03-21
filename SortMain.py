# 快速排序
# 功能: 对数字数组进行升序排序
# 参数: arr - 待排序的数字数组
# 返回值: sortedArr - 排序后的升序数组
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


if __name__ == '__main__':
    # 测试数组: 统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组: ", testArr)
    
    # 成员调用自己的算法: 后续在此处添加代码
    # 调用快速排序算法
    result = zcQuickSort(testArr)
    print("zc-快速排序算法排序结果: ", result)