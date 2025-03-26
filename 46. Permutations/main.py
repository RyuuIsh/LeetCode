class Solution:
    def permute(self, nums):
        def backtrack(path, remaining, result):
            if not remaining:
                result.append(path)
                return
            
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:], result)
        
        result = []
        backtrack([], nums, result)
        return result
