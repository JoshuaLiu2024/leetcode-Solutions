class Solution_1:
    def trap(self, height: List[int]) -> int:
        # 方法一：暴力解法
        # 对于每个height，遍历其左右元素，找到leftmax和rightmax。
        # 如果leftmax<=height[i]或者rightmax<=height[i]，说明当前列无法储存雨水
        # 否则，当前列能储存的水量为min(leftmax,rightmax)-height[i]
        def getmax(i, height:List):
            # 返回两个值，分别为leftmax,rightmax
            leftmax, rightmax = 0, 0
            for k in range(i):
                if height[k] > leftmax :
                    leftmax = height[k]
            for k in range(i+1,len(height)):
                if height[k] > rightmax :
                    rightmax = height[k]
            return leftmax, rightmax
        
        water = 0
        for i in range(len(height)):
            leftmax, rightmax = getmax(i,height)
            if leftmax <= height[i] or rightmax <= height[i]:
                continue
            else:
                water += min(leftmax,rightmax) - height[i]
        
        return water
    
class Solution_2:
    def trap(self, height: List[int]) -> int:
        # 方法二：双指针
        # 遍历数组，从左往右得到leftmax[i]，从右往左得到rightmax[i]
        # 然后再遍历数组，对每个height[i]，用leftmax[i],rightmax[i],height[i]得到对应水量

        leftmax, rightmax = [0] * len(height), [0] * len(height)
        for i, height_num in enumerate(height):
            if i == 0 :
                leftmax[i] = height_num
            else:
                leftmax[i] = max(height_num, leftmax[i - 1])
        for i, height_num in enumerate(reversed(height)):
            if i == 0 :
                rightmax[i] = height_num
            else:
                rightmax[i] = max(height_num, rightmax[i - 1])
        rightmax = list(reversed(rightmax))
        water = 0
        for i, height_num in enumerate(height):
            if leftmax[i] < height_num or rightmax[i] < height_num:
                continue
            else:
                water += min(leftmax[i], rightmax[i]) - height_num
        return water
    

class Solution_3:
    def trap(self, height: List[int]) -> int:
        # 方法三：双指针进阶
        # 双指针指向数组两侧
        left = 0
        right = len(height) - 1
        water = 0

        leftmax,rightmax = height[left], height[right]
        while left < right :
            if leftmax < rightmax:
                water += leftmax - height[left]
                left += 1
                leftmax = max(leftmax, height[left])
            else:
                water += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax, height[right])
        
        return water