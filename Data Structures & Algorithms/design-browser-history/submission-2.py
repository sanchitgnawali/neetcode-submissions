# Using dynamic array. This is the most efficient solution
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_position = 0
       

    def visit(self, url: str) -> None:
        self.current_position += 1
        self.history = self.history[:self.current_position]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_position = max(0, self.current_position - steps)
        return self.history[self.current_position]

    def forward(self, steps: int) -> str:
        self.current_position = min(len(self.history)-1, self.current_position+steps)
        return self.history[self.current_position]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)