# from copy import deepcopy
#
# def checkVaild(check_list,num):
#     mylist = deepcopy(check_list)
#     mylist.remove(num)
#     mylist.sort()
#     for phone in mylist:
#         idx = 0
#         phone = str(phone)
#         num = str(num)
#         while idx < len(num):
#             if idx == len(phone)-1 and num[idx] == phone[idx]:
#                 return False
#
#             if num[idx] != phone[idx]:
#                 break
#             idx += 1
#     return True
#
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     phone_list = []
#     for _ in range(n):
#         phone_list.append(int(input()))
#
#     flag = True
#     for phone in phone_list:
#         flag = checkVaild(phone_list,phone)
#
#         if flag == False:
#             print("NO")
#             break
#     if flag == True:
#         print("YES")

# # 단순 구현은 시간초과 발생 -> 트라이 (Trie) 로 풀이
#
class Node(object):
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        cur_node = self.head

        for char in string:

            if char not in cur_node.children:
                cur_node.children[char] = Node(char) # 현재 노드의 칠드런에 자신의 글자가 없으면 그것으로 자식노드 생성
            cur_node = cur_node.children[char] # 있으면 그 노드로 이동
            if cur_node.data != None:
                return False

        cur_node.data = string # for문 전체 수행 이후 해당 문자열을 삽입
        return True

    # def search(self, string):
    #     cur_node = self.head
    #     for char in string:
    #         if char in cur_node.children:
    #             cur_node = cur_node.children[char]
    #         else:
    #             return False
    #
    #     if cur_node.data != None:
    #         return True





t = int(input())
for _ in range(t):
    n = int(input())
    phone_list = []
    trie = Trie()
    for _ in range(n):
       phone_list.append(str(input()))

    phone_list.sort()
    flag = True
    for phone in phone_list:
        if trie.insert(phone) == False:
            flag = False
            print("NO")
            break
    if flag == True:
        print("YES")


