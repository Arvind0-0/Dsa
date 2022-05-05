class MyStack:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        top = self.queue[-1]
        self.queue = self.queue[:-1]
        return top
    
    def top(self) -> int:
        return self.queue[-1]    

    def empty(self) -> bool:
        return False if self.queue else True
