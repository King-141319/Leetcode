class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        firstPointer = 0
        lastPointer = len(height) - 1
        while firstPointer < lastPointer:
            vol = (lastPointer - firstPointer) * min(height[firstPointer],height[lastPointer])
            if maxVol < vol:
                maxVol = vol
            if height[firstPointer] < height[lastPointer]:
                firstPointer += 1
            else:
                lastPointer -= 1
        return maxVol