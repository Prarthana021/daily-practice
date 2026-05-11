class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

    def get(self, key, timestamp):
        value= self.store.get(key,[])
        l=0
        r=len(value)-1
        res=""

        while l<=r:
            m=(l+r)//2
            if value[m][1] <= timestamp:
                res=value[m][0]
                l=m+1
            else:
                r=m-1
        return res
    
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)