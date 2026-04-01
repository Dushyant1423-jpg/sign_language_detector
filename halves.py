# # interleave the two halves of a queue 
# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError("Queue is empty")

#     def size(self):
#         return len(self.items)

#     def interleave_halves(self):
#         if self.size() % 2 != 0:
#             raise ValueError("Queue must have an even number of elements to interleave")
        
#         half_size = self.size() // 2
#         first_half = self.items[:half_size]
#         second_half = self.items[half_size:]

#         interleaved = []
#         for i in range(half_size):
#             interleaved.append(first_half[i])
#             interleaved.append(second_half[i])

#         self.items = interleaved
# # test
# q = Queue() 
# for i in range(1, 9):
#     q.enqueue(i)
# q.interleave_halves()
# print(q.items)  # Output: [1, 5, 2, 6, 3, 7, 4, 8]        


from collections import deque

def interleave(q):
    n = len(q)
    
    if n % 2 != 0:
        print("Queue must be even")
        return

    half = n // 2
    first_half = deque()

    # first half निकालो
    for _ in range(half):
        first_half.append(q.popleft())

    # interleave
    while first_half:
        q.append(first_half.popleft())
        q.append(q.popleft())

    return q


# test
q = deque([1,2,3,4,5,6,7,8])
print(interleave(q))