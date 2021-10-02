class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkList():
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def append(self, val):
        node = ListNode(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode()
        res = prehead
        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next
        res.next = l1 if l1 else l2
        return prehead.next

list1, list2 = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]
l1, l2 = SingleLinkList(), SingleLinkList()
for n in list1:
    l1.append(n)
for n in list2:
    l2.append(n)

SS = Solution()
res = SS.mergeTwoLists(l1.head, l2.head)
while res is not None:
    print(res.val)
    if res.next is not None:
        res = res.next
    else:
        break
