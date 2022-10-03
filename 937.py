from typing import List
from functools import reduce

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        class Log:
            def __init__(self, id: str, content: str):
                self.id = id
                self.content = content

            def to_str(self):
                return self.id + " " + self.content

        letter_logs: List[Log] = []
        digit_logs: List[Log] = []

        for log in logs:
            first_space = log.find(" ")
            second_space = log.find(" ", first_space + 1)
            id = log[:first_space]
            content = log[first_space + 1:]
            first_log = log[first_space + 1 : second_space]

            if first_log.isalpha():
                letter_logs.append(Log(id, content))
            else:
                digit_logs.append(Log(id, content))

        letter_logs.sort(key=lambda l: (l.content, l.id))

        return reduce(lambda acc, cur: acc + [cur.to_str()], letter_logs, []) + reduce(lambda acc, cur: acc + [cur.to_str()], digit_logs, [])




print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))






