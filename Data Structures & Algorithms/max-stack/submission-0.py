class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.removed = set()
        self.count = 0

    # define helper functions to cleanup stack and heap
    def clean_stack(self):
        while self.stack and self.stack[-1][1] in self.removed:
            _, idx = self.stack.pop()
            self.removed.remove(idx)

    
    def clean_heap(self):
        # implement clean heap
        while self.heap and -self.heap[0][1] in self.removed:
            _, idx = heapq.heappop(self.heap)
            self.removed.remove(-idx)



    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.count))
        self.stack.append((x, self.count))
        self.count += 1

    def pop(self) -> int:
        self.clean_stack()

        num, idx = self.stack.pop()
        self.removed.add(idx)

        return num
        

    def top(self) -> int:
        self.clean_stack()

        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.clean_heap()

        return -self.heap[0][0]

    def popMax(self) -> int:
        self.clean_heap()

        num, idx = heapq.heappop(self.heap)
        self.removed.add(-idx)

        return -num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
