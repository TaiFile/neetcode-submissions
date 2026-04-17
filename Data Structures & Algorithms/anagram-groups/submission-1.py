class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_count = defaultdict(list)

        for words in strs:
            key = tuple(sorted(words))
            strs_count[key].append(words)

        return list(strs_count.values())