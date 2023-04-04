from collections import deque
from queue import Queue

class MaxQueue1:

    def __init__(self):
        self.data=deque(maxlen=10000)

    def max_value(self) -> int:
        return max(self.data) if self.data else -1

    def push_back(self, value: int) -> None:
        self.data.append(value)

    def pop_front(self) -> int:
        
        return self.data.popleft() if self.data else -1
        
class MaxQueue:

    def __init__(self):
        self.helper=deque(maxlen=10000)
        self.data=Queue(10000)

    def max_value(self) -> int:
        return self.helper[0] if self.helper else -1

    def push_back(self, value: int) -> None:
        while(self.helper and self.helper[-1]<value):
            self.helper.pop()
        self.helper.append(value)
        self.data.put(value)

    def pop_front(self) -> int:
        if self.data.empty():
            return -1
        ans = self.data.get()
        if ans == self.helper[0]:
            self.helper.popleft()
        return ans

