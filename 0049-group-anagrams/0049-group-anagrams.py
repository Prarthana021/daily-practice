class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mymap={}
        for s in strs:
            sortedS=''.join(sorted(s))
            if sortedS in mymap:
                mymap[sortedS].append(s)
            else:
                mymap[sortedS]=[s]
        return list(mymap.values())





        res=defaultdict(list)
        #list is passed as a function 
        #defaultdict will call list() whenever a key is missing
        #{aet: [eat, tea], ant:[tan,ant]}
        for s in strs:
            sortedS= ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
