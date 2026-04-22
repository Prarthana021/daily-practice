class MyHashMap:

    def __init__(self):
        self.hass={}
        

    def put(self, key: int, value: int) -> None:
        self.hass[key]=value
        

    def get(self, key: int) -> int:
        return (self.hass.get(key,-1))
        

    def remove(self, key: int) -> None:
        if key in self.hass:
            del self.hass[key]
 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)