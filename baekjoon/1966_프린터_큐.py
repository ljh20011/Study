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
        return self.queue[0]

def sol(doc, k):
    queue = Queue(doc)
    queue_sort = doc.copy()
    queue_sort.sort()
    chk = [0] * len(doc)
    chk[k] = 1
    cnt = 0
    while(queue.size()):

        if queue.top() == queue_sort[-1]: #우선 순위 같은 경우
            if chk[0] == 1:
                return cnt + 1
            queue.pop()
            queue_sort.pop()
            chk.pop(0)
            cnt += 1
        else: # 다른 경우
            queue.push(queue.pop())
            chk.append(chk.pop(0))


n = int(input())

for i in range(n):
    info = list(map(int, input().split()))
    doc = list(map(int, input().split()))
    print(sol(doc, info[1]))
