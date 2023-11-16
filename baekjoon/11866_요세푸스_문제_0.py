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

def sol(n, k):
    queue = list(range(1,n+1))
    queue = Queue(queue)
    ans = []
    cnt = 1
    while(queue.size() != 0):
        if cnt == k:
            top = queue.pop()
            ans.append(top)
            cnt = 1
        else:
            top = queue.pop()
            queue.push(top)
            cnt += 1
    return ans

n, k = map(int,input().split())
ans = sol(n, k)
print("<", end="")
for i in range(n):
    if i == n-1:
        print(ans[i], end=">")
    else:
        print(ans[i], end=', ')