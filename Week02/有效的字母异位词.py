
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = collections.defaultdict(int)
        if len(s)!= len(t):
            return False
        for ind in range(0,len(s)):
            hashmap[s[ind]] +=1
            hashmap[t[ind]] -=1
        for ind in hashmap:
            if hashmap[ind]<0:
                return False
        return True