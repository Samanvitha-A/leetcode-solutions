from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        q = deque()      # stores indices
        l = r = 0

        while r < len(nums):

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove left element if it is outside window
            if l > q[0]:
                q.popleft()

            # Window size reached k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
        