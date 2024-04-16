from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            p1, p2 = i + 1, len(nums) - 1
            if a == nums[i - 1] and i > 0:
                    continue
            while(p1 < p2):
                sumation = a + nums[p1] + nums[p2]
                if sumation > 0:
                    p2 -= 1
                elif sumation < 0:
                    p1 += 1
                else:
                    combination = [a, nums[p1], nums[p2]]
                    result.append(combination)
                    p1 += 1
                    while(nums[p1] == nums[p1 - 1] and p1 < p2):
                        p1 += 1

        return result