class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previousGroupEnd = dummy

        while True:
            # Find the last node in the next group of k
            groupEnd = previousGroupEnd

            for _ in range(k):
                groupEnd = groupEnd.next
                if not groupEnd:
                    return dummy.next

            nextGroupStart = groupEnd.next
            groupStart = previousGroupEnd.next

            # Reverse this group
            prev = nextGroupStart
            curr = groupStart

            while curr != nextGroupStart:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            # Connect previous group to newly reversed group
            previousGroupEnd.next = groupEnd

            # Original groupStart is now the end of the reversed group
            previousGroupEnd = groupStart