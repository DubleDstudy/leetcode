class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            comp = ''.join(sorted(word))
            if comp not in anagram:
                anagram[comp] = [word]
            else:
                anagram[comp].append(word)
        ans = []
        for v in anagram.values():
            ans.append(v)
        return ans