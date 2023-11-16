class Queue():
    def __init__(self, doc):
        self.queue = doc
    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        return self.queue

    def push(self, value):
        return self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue.sort(reverse=True)[0]

def sol(queue):

    return

n = int(input())

for i in range(n):
    info = list(map(int, input().split()))
    doc = []
    for j in range(info):
        doc.append(int(input))
    queue = Queue(doc)
    sol(queue)

