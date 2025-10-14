class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict={}
        for str in strs:
            #Since lists are unhashable (mutable), you can't use them as dictionary keys, which will cause an error. The fix:
#Convert the sorted list back to a string using ''.join()
            sorted_word = ''.join(sorted(str))

            if sorted_word in mydict:
                mydict[sorted_word].append(str)
            else:
                mydict[sorted_word]=[str]

        return list(mydict.values())