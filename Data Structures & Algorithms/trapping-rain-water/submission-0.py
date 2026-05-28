class Solution:
    def trap(self, height: List[int]) -> int:

        l_wall = 0 # stores idx
        total_area = 0
        n = len(height)

        while l_wall < n -2:
            # look for l_wall
            while l_wall < n - 2 and height[l_wall + 1] >= height[l_wall]:
                l_wall += 1

            # found l_wall
            # look for right wall
            r_wall = l_wall + 1
            pos_r_wall = max(height[l_wall:])
            min_height = min(height[l_wall:])

            # look for taller wall
            while r_wall < n and height[r_wall] < height[l_wall]:
                r_wall += 1

            # if no taller wall, set to tallest possible wall
            if r_wall == n:
                max_idx = l_wall + 1
                for i in range(l_wall + 1, n):
                    if height[i] > height[max_idx]:
                        max_idx = i

                r_wall = max_idx
            

            area = min(height[l_wall], height[r_wall]) * (r_wall-l_wall - 1)

            for i in range(l_wall + 1, r_wall):
                area -= height[i]
        
            total_area += area

            l_wall = r_wall

        return total_area

            