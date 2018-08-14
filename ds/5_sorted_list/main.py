import bisect

lst = [9, 1, 8, 2, 7]
o_lst = []

for num in lst:
    bisect.insort(o_lst, num)
    print(o_lst)
