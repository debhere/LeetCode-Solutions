'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        curr = head
        if not (list1 and list2):
            return list1
        if list1 and not list2:
            return list1
        if not list1 and list2:
            return list2
        # pt1, pt2 = None, None
        while list1 and list2:
            pt1, pt2 = (list1, list2) if list1.val < list2.val else (list2, list1)
            list1 = list1.next
            list2 = list2.next
            curr = ListNode(pt1, pt2)
        return curr


l10 = ListNode(3)
l12 = ListNode(2, l10)
l13 = ListNode(1, l12)

l20 = ListNode(3)
l21 = ListNode(2, l20)
l23 = ListNode(1, l21)

sol = Solution()
# print(sol.mergeTwoLists([1, 2, 4], [1, 3, 4]))
# print(sol.mergeTwoLists([], []))
# print(sol.mergeTwoLists([], [0]))
# print(sol.mergeTwoLists(l13, l23))
print(l23.val)
print(l23.next.val)
print(l23.next.next.val)

print(sol.mergeTwoLists(l13, l23).val)
