class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen={}
        lst=[]
        for str in strs:
            new_str= "".join(sorted(str))
            if new_str in seen:
                seen[new_str].append(str)
            else:
                seen[new_str]=[str]
        return list(seen.values())