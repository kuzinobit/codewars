def queue_time(customers, n):
    queue = [0]*n
    for time in customers:
        queue[queue.index(min(queue))] += time
    return max(queue)

print(queue_time([1,2,3,4],5))
print(queue_time([2,2,3,3,4,4], 2))