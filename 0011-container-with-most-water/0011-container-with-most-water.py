class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        
        max_area = 0
        while(p1 < p2):
            h = height[p1] if height[p1] < height[p2] else height[p2]
            w = p2 - p1
            area = h * w
            
            if area > max_area:
                max_area = area
            
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
                
        return max_area