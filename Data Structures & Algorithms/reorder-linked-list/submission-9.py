# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        quick = head
        slow = head

        while quick.next and quick.next.next:
            quick = quick.next.next
            slow = slow.next

        firstHalf = head
        secondHalf = slow.next
        
        slow.next = None

        prev = None
        while secondHalf:
            nextNode = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nextNode

        secondHalf = prev
        
        while secondHalf:
            firstHalfNext = firstHalf.next
            secondHalfNext = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = firstHalfNext

            firstHalf = firstHalfNext
            secondHalf = secondHalfNext

