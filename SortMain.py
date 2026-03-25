if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    # 选择排序
    # 选择排序
    # 功能：对数字数组进行升序排序
    # 参数：arr - 待排序的数字数组
    # 返回值：sortedArr - 排序后的升序数组
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
