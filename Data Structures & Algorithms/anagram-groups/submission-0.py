class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in table:
                table[sorted_word] = []
            table[sorted_word].append(word)

        return list(table.values())