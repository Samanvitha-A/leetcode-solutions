class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(index, path, total):
            if total == target:
                ans.append(path[:])
                return
            if index == len(candidates) or total > target:
                return

            path.append(candidates[index])
            dfs(index, path, total + candidates[index])
            path.pop()

            dfs(index + 1, path, total)

        dfs(0, [], 0)
        return ans
        