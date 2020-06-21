class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for ind, num in enumerate(nums):
            if target - num not in dic:
                dic[num] = ind
            elif target - num in dic and dic[target - num] != ind:
                return [dic[target - num], ind]
