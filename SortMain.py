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


if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    sortedArr = fzhInsertionSort(testArr)
    print("插入排序结果：", sortedArr)
    
    # 验证排序正确性
    print("验证（Python内置排序）：", sorted(testArr))
    print("排序正确：" if sortedArr == sorted(testArr) else "排序错误！")