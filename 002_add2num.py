class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = n = ListNode(0);
        c = 0
        while l1 or l2 or c:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            c,val = divmod(v1+v2+c, 10)
            n.next = ListNode(val)
            n = n.next
        return r.next
