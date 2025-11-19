"""
LeetCode Problem: 83. Remove Duplicates from Sorted List

Algorithm: Single Pass Iteration approach using two pointers (current and current.next)

Time Complexity: O(n), where n is the number of nodes in the linked list.=@

Space Complexity: O(1), as we are modifying the list in place without using extra space.
"""

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
    
if __name__ == "__main__":
    pass

"""
Optimization: The current implementation is already optimal with O(n) time complexity and O(1) space complexity. No further optimizations are necessary.
"""