class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False


        s1arr=[0]*26
        s2arr=[0]*26

        for i in range(len(s1)):
            indexs1= ord(s1[i])-ord('a')
            indexs2= ord(s2[i])-ord('a')

            s1arr[indexs1]+=1
            s2arr[indexs2]+=1
        
        for i in range(len(s2)-len(s1)):
            if(s1arr==s2arr):
                return True

            else:
                indexr= ord(s2[i+len(s1)])-ord('a')
                indexl=ord(s2[i])-ord('a')

                s2arr[indexr]+=1
                s2arr[indexl]-=1
        
        return s2arr==s1arr

















