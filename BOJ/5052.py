from copy import deepcopy

def checkVaild(check_list,num):
    mylist = deepcopy(check_list)
    mylist.remove(num)
    mylist.sort()
    for phone in mylist:
        idx = 0
        phone = str(phone)
        num = str(num)
        while idx < len(num):
            if idx == len(phone)-1 and num[idx] == phone[idx]:
                return False

            if num[idx] != phone[idx]:
                break
            idx += 1
    return True


T = int(input())
for _ in range(T):
    n = int(input())
    phone_list = []
    for _ in range(n):
        phone_list.append(int(input()))

    flag = True
    for phone in phone_list:
        flag = checkVaild(phone_list,phone)

        if flag == False:
            print("NO")
            break
    if flag == True:
        print("YES")

# # 단순 구현은 시간초과 발생 -> 트라이 (Trie) 로 풀이
#
# class Node(object):
#     def __init__(self,key,data = None):
#         self.key = key
#         self.data = data
#         self.children = {}
#
#
#     def insert(self,string):
#         cur_node = self.head
#
#         for char in string:
#             if char not in cur_node.children:
#                 cur_node.children[char] = Node(char)
#             cur_node = cur_node.children[char]
#         cur_node.data = string
#
#
#


