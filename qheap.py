
import heapq

Q = int(input())

min_val = 1000000000
min_values = set()
min_heap = []
removed = set()
added = set()

for _ in range(Q):
    inp = input()
    if inp == '3':
        while min_heap[0] in removed:
            heapq.heappop(min_heap)
        print(min_heap[0])
    else:
        op, val = inp.split()
        if op == '1':
            
            heapq.heappush(min_heap, int(val))
            
        else:
            removed.add(int(val))
            

