from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 将访问的 key 移到末尾，表示最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新值并移到末尾
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # 容量满，移除最久未使用的（头部）
            self.cache.popitem(last=False)
        # 插入或更新 key-value 对（默认插入到末尾）
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)