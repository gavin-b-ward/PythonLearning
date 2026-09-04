from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l_heights = [0] * len(height)
        r_heights = [0] * len(height)

        cur_l_max = 0
        for i, h in enumerate(height):
            l_heights[i] = cur_l_max
            if cur_l_max < h: 
                cur_l_max = h
        cur_r_max = 0 
        for i in range(len(height) - 1, -1, -1):
            r_heights[i] = cur_r_max
            if cur_r_max < height[i]:
                cur_r_max = height[i]

        t = 0
        for i in range(len(height)):
            w = min(l_heights[i], r_heights[i]) - height[i]
            if w < 0:
                w = 0
            t += w
        return t
