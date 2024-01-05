class Solution:
    def getkey(self, string):
        charconuter = [0] * 26
        
        offset = ord('a')
        for char in string:
            charconuter[ord(char) - offset] += 1
        return tuple(charconuter)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            groups[self.getkey(string)].append(string)
        
        return groups.values()