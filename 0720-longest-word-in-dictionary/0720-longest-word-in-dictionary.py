class Solution:
    def longestWord(self, words):
        words.sort()
        valid = {""}
        ans = ""

        for word in words:
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans
        