class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        return self.data.insert(0, item)
    
    def dequeue(self):
        return self.data.pop()
    


