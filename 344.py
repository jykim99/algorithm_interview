from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        length = length // 2

        for i in range(0, length):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp

