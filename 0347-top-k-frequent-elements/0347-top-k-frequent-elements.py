from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # constuct buckets to store elements in based on thier frequency
        buckets = [[] for _ in range(len(nums) + 1)] 
        
        # populate the buckets with the keys given thier frequency
        for num, freq in collections.Counter(nums).items():
            buckets[-freq].append(num) 
        
        # for nums=[1, 1, 1, 2, 2, 3, 4, 4, 4] --> Counter={1:3, 2:2, 3:1, 4:3} --> 
        # buckets=[[], [], [1, 4], [2], [3]]
        # unfold and limit to k elements --> [1, 4, 2, 3][:k]
        return list(itertools.chain(*buckets))[:k]