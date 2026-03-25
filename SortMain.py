if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    # 功能：对数字数组进行升序排序（冒泡排序）
    # 参数：arr - 待排序的数字数组
    # 返回值：sortedArr - 排序后的升序数组
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
        


