class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        seen={}
        for str in strs:
            new_str= "".join(sorted(str))
            if new_str not in seen:
                
                seen[new_str]=[str]
            else:
                seen[new_str].append(str)
        
        for item  in seen.values():
            res.append(item)
        return res
        
      