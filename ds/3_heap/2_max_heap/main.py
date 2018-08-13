import heapq

def heapify(lst):
    get_neg_lst(lst)
    heapq.heapify(lst)
    get_neg_lst(lst)

def get_neg_lst(lst):
    cur_ind = 0
    while(cur_ind < len(lst)):
        lst[cur_ind] = (-1)*(lst[cur_ind])
        cur_ind = cur_ind+1

def pop(lst):
    get_neg_lst(lst)
    num = heapq.heappop(lst)
    get_neg_lst(lst)
    return (-1)*num

def push(lst, num):
    get_neg_lst(lst)
    num = num*(-1)
    heapq.heappush(lst, num)
    get_neg_lst(lst)

lst = [4, 2, 5, 3]
print("Raw list : " + str(lst))

# Heapify
heapify(lst)
print("Post Heapify : " + str(lst))

# Pop
num = pop(lst)
print("Popped num : " + str(num))
print("post pop : " + str(lst))

# Push 5
push(lst, 5)
print("Push 5 : " + str(lst))

# Push 1
push(lst, 1)
print("push 1 : " + str(lst))








