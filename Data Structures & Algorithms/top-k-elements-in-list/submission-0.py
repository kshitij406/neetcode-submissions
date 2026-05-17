class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = dict(Counter(nums))
        sorted_keys = [key for key, value in sorted(frequency_dict.items(), key=lambda item: item[1])]
        
        return sorted_keys[-k:]