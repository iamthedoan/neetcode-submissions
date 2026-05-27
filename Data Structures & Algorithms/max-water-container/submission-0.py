class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # get two largest numbers
        # area is smaller value * distance
        
        # brute force
        # calculate all pairs and distance and compare
        max_area = 0

        for i,a in enumerate(heights):
            for j,b in enumerate(heights):
                if i != j:
                    length = abs(i - j)
                    area = min(a,b) * length
                    if area > max_area:
                        max_area = area

        return max_area





