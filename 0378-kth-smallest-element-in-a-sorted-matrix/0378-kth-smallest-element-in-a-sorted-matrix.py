import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(heap)[0]
        