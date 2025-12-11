nums = [1,1,1]
k = 2
length = len(nums)
left, right = 0, 0
index = 0

while left <= length :
    if left < right :
        sumup = 0
        for i in range(left, right+1):
            sumup += nums[i]
        
        if sumup < k :
            if right < length :
                right += 1
            else :
                break
        elif sumup == k :
            index += 1
        else :
            left += 1
    else :
        if nums[left] == k :
            index += 1
        elif nums[left] < k :
            right += 1
        else :
            left += 1
            right += 1

print(index)