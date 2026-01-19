class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        #list is passed as a function 
        #defaultdict will call list() whenever a key is missing
        #{aet: [eat, tea], ant:[tan,ant]}
        for s in strs:
            sortedS= ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
