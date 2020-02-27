from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.storage or self.storage[key] == None:
            return None
        self.set(key, self.storage[key].value)
        return self.storage[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            self.dll.delete(node)
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
        elif self.limit == len(self.dll):
            for v, k in self.storage.items():
                if k.value == self.dll.tail.value:
                    self.storage[v] = None
            self.dll.remove_from_tail()
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
        else:
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
        # for i, k in self.storage.items():
        #     print(i, k.value)


cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.get("item1")
cache.set("item4", "d")
cache.get("item1")
cache.get("item3")
cache.get("item4")
print(cache.storage)
