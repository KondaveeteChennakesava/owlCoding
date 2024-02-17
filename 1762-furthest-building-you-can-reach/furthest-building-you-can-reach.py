class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        low,high = 0,n
        def check(p):
            rbricks = bricks
            need = []
            for i in range(p):
                if heights[i+1] > heights[i]:
                    need.append(heights[i+1] - heights[i])
            need.sort(reverse = True)
            while need and need[-1] <= rbricks:
                rbricks -= need[-1]
                need.pop()
            return ladders >= len(need)
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                low = mid
            else:
                high = mid
        return low