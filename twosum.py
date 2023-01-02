class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for position in range(len(nums)):
            currentNumber = nums[position]
            check = target - currentNumber
            if map.has_key(check):
                return position, map[check]
            map[currentNumber] = position
