class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_index = 0
        cookie_index = 0
        content_children = 0
        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                content_children += 1
                child_index += 1
            cookie_index += 1
        return content_children