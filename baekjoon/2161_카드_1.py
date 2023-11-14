class Queue():
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        return self.queue

    def push(self, value):
        return self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)

def sol(queue):
    for i in range(n):
        queue.push(i)

    while queue.size() > 0:
        print(queue.pop() + 1)
        if queue.size() == 0:
            break
        queue.push(queue.pop())
    return

n = int(input())

queue = Queue()
sol(queue)
