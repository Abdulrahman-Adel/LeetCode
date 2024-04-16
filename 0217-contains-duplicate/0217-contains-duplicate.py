class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for i in nums:
            placement = counter.get(i, 0)
            if placement:
                return True
            counter[i] = placement + 1
        return False