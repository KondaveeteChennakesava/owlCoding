class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happy = sorted(happiness)
        happiness = 0
        for i in range(k):
            value = sorted_happy.pop() - i
            if value <= 0:return happiness
            happiness += value
        return happiness