class Node:
    def __init__(self, key, val, freq=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self._sentinel = Node(0, 0)
        self._len = 0
        self._sentinel.prev, self._sentinel.next = self._sentinel, self._sentinel

    def __len__(self):
        return self._len

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._len -= 1
        return node

    def remove_last(self):
        return self.remove(self._sentinel.prev)

    def insert_first(self, key, val, freq):
        node = Node(key, val, freq, self._sentinel, self._sentinel.next)
        node.next.prev = node
        self._sentinel.next = node
        self._len += 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self._min_freq = 0
        self._nodes = {}
        self._freqs = {}

        self._capacity = capacity
        self._size = 0

    def get(self, key: int) -> int:
        if key not in self._nodes:
            return -1
        node = self._nodes[key]

        # adjust the frequencies lists
        self._freqs[node.freq].remove(node)
        if node.freq + 1 not in self._freqs:
            self._freqs[node.freq + 1] = DoublyLinkedList()
        new_node = self._freqs[node.freq + 1].insert_first(node.key, node.val, node.freq + 1)
        self._nodes[key] = new_node

        if self._min_freq == node.freq and len(self._freqs[node.freq]) == 0:
            self._min_freq = node.freq + 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._nodes:
            self.get(key)
            self._nodes[key].val = value
            return
        if self._size < self._capacity:
            self._size += 1
        else:
            evicted_node = self._freqs[self._min_freq].remove_last()
            self._nodes.pop(evicted_node.key)
        if 1 not in self._freqs:
            self._freqs[1] = DoublyLinkedList()
        node = self._freqs[1].insert_first(key, value, 1)
        self._nodes[key] = node
        self._min_freq = 1