import heapq

lst = [4, 2, 3, 6]
print("raw list : " + str(lst))

# Heapify
heapq.heapify(lst)
print("post heapify : " + str(lst))

# Pop
num = heapq.heappop(lst)
print("popped num : " + str(num))
print("Post pop : " + str(lst))

# Push 1
heapq.heappush(lst, 1)
print("pushed 1 : " + str(lst))

# Push 2
heapq.heappush(lst, 2)
print("pushed 2 : " + str(lst))
