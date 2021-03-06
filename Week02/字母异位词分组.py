class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
        return list(hashmap.values())