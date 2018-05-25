# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        before = None
        first = head
        second = head.next
        after = second.next if second is not None else None
        while first is not None:
            if second is not None:
                # Can switch (pair exists)
                # Switch
                if before is not None:
                    before.next = second
                else:
                    # This is first pair
                    head = second
                first.next = after
                second.next = first
                # Update for next round
                before = first
                first = after
                second = first.next if first is not None else None
                after = second.next if second is not None else None
            else:
                # No more to switch (last one left)
                if before is not None:
                    before.next = first
                else:
                    # This is first pair
                    head = first
                break

        return head

