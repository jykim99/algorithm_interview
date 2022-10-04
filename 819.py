from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        splited = []

        last_idx = -1
        for i in range(0, len(paragraph)):
            if paragraph[i].isalpha():
                if i == len(paragraph) - 1:
                    splited.append(paragraph[last_idx + 1: i + 1])
            else:
                if last_idx + 1 == i:
                    last_idx = i
                else:
                    splited.append(paragraph[last_idx + 1: i])
                    last_idx = i

        counter = Counter(splited)

        for word in banned:
            try:
                counter.pop(word)
            except KeyError:
                pass

        return counter.most_common()[0][0]

print(Solution().mostCommonWord(paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"]))