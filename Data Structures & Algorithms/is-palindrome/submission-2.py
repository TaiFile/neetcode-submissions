class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in range(len(s)):
            char = s[i].lower()
            if char.isalnum():
                string.append(char)

        sizeString = len(string)
        # for i in range((sizeString // 2)):
        #     if string[i] != string[sizeString - i - 1]:
        #         return False
        return string == string[::-1]