### 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(0,len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
        out =j+1
        return out


