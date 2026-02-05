#create node, initialize everything, in the lru class initialize capacity,cache
#and create 2 dummy nodes left and write , wirte get function check if key exists, move to mru and return, write put function check if key already exists yes then remove the key create a node and move to mru , else if capacity exceeded then find the lru and delete it from the hash map and node both using key , finally define the remove and insert function, remove removes from whichever element is the given node since its task is to remove the current node just break it form the chain then in insert function insert it to the right most section where prev=right.prev, nxt=right.nxt

class Node:
    def __init__(self,key:int,value:int):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
#cache : key  →  Node(key, value)
#hashmap key=key, value = Node object(k,v)
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

        
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev


    def insert(self,node):
        prev= self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev=node
        node.prev=prev
        node.next=nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]











        
