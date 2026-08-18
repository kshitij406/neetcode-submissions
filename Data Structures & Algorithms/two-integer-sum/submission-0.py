class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            seen[num] = index
            diff = target - num
            if diff in seen:
                if seen[diff] != seen[num]:
                    return [seen[diff], seen[num]]