from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, len(s) // 2):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp


