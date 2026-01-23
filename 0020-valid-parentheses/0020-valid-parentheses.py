class Solution:
    def isValid(self, s: str) -> bool:
        mymap={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s: #i=each character in string
            if i in mymap:
                if stack and stack[-1]== mymap[i]: #if stack meaning if stack is not empty and -1 means last element and s[i] means value of dict mymap
                    stack.pop() #pops last element
                else:
                    return False #for cases like ] starts with closing bracket 
            else:
                stack.append(i)
        return True if not stack else False #return true if stack is empty






            




        