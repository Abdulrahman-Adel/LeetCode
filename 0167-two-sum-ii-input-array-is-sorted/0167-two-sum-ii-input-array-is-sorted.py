class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = 0

        for i in range(len(numbers)):
            current = numbers[i]
            if target - current in numbers[i+1:]:
                pointer_1 = i
                pointer_2 = i + numbers[i+1:].index(target - current) + 1
                break
        return (pointer_1 + 1, pointer_2 + 1)