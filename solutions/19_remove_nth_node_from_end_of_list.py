# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Get index of nodes
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        length = len(nodes)
        if n == length:
            # Remove first node
            head = head.next
        elif n == 0:
            # Remove last node
            nodes[length - 2].next = None
        else:
            # Remove some nodes in between
            target = nodes[length - n]
            prev = nodes[length - n - 1]
            prev.next = target.next

        return head


def convert_to_linked_list(a):
    head = None
    prev = None
    for i in range(len(a)):
        if prev == None:
            head = ListNode(a[i])
            prev = head
        else:
            curr = ListNode(a[i])
            prev.next = curr
            prev = curr
    return head


def convert_to_list(head):
    a = []
    while head is not None:
        a.append(head.val)
        head = head.next
    return a


head = Solution().removeNthFromEnd(convert_to_linked_list([1, 2, 3, 4, 5]), 5)
print(convert_to_list(head))
