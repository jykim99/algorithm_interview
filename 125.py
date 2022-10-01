def main():
    print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        li = list(filter(str.isalnum, list(s)))

        for i in range(0, len(li) // 2):
            if li[i] != li[len(li) - i - 1]:
                return False

        return True


if __name__ == '__main__':
    main()
