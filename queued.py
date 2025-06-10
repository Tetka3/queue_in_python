class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        return self.data.insert(0, item)
    
    def dequeue(self):
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data) 
    


