class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_result_digit = ListNode(None)
        result_prev = current_result_digit
        carry = 0

        # Add normally
        while l1 is not None and l2 is not None:
            digit_sum, carry = self._add(l1.val, l2.val, carry)
            current_result_digit.next = ListNode(digit_sum)
            current_result_digit = current_result_digit.next
            l1 = l1.next
            l2 = l2.next

        # Handle leading digits
        if l1 is not None:
            lead = l1
        elif l2 is not None:
            lead = l2
        else:
            lead = None
        while lead is not None:
            digit_sum, carry = self._add(0, lead.val, carry)
            current_result_digit.next = ListNode(digit_sum)
            current_result_digit = current_result_digit.next
            lead = lead.next

        # Handle last carry
        if carry > 0:
            current_result_digit.next = ListNode(carry)

        return result_prev.next

    def _add(self, num_1, num_2, carry):
        """
        All params are >= 0 and < 10

        :type num_1: int
        :type num_2: int
        :type carry: int
        :return: digit_sum, carry
        """
        num_sum = num_1 + num_2 + carry
        return num_sum % 10, num_sum // 10
