class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happiness.reverse()
        happy = 0
        print(happiness)
        for i in range(k):
            if happiness[i] - i > 0:
                happy +=  happiness[i] - i
        return happy