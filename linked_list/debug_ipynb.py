class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head_stack = []
        while head:
            head_stack.append(head)
            head = head.next
        cur = ListNode()
        head2 = cur
        while head_stack:
            cur.next = head_stack.pop()
            # cur = cur.next
            # head_stack.pop()
        return head2.next


n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

SS = Solution()
# res = SS.reverseList(n1)
# print(res)
# class Test:
#     def __init__(self, x):
#         self.x = x
#     def ret_num(self):
#         return self.x
#     def change(self, y):
#         self.x = y

# c1 = Test(1)
# c2 = c1
# print('c1: {:d}, c2: {:d}'.format(c1.ret_num(), c2.ret_num()))
# c1.change(2)
# print('c1: {:d}, c2: {:d}'.format(c1.ret_num(), c2.ret_num()))
