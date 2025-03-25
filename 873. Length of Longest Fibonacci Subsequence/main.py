class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {val: idx for idx, val in enumerate(arr)}
        dp = {}
        max_len = 0
        
        for j in range(len(arr)):
            for i in range(j):
                k = index.get(arr[j] - arr[i])
                if k is not None and k < i:
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])
        
        return max_len if max_len >= 3 else 0

