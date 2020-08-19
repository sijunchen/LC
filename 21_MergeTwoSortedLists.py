# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        #ceate a new ll
        l3 = ListNode()

        stack = []
        stack.insert(0, l1.va)

        while stack:
            if stack[0] <= l2.val:
                l3.val = stack.pop(0)
                
            else:


            pass

def main():
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l11.next = l12
    l12.next = l13

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    s = Solution()
    print(s.mergeTwoLists(l11, l21))

if __name__ == "__main__":
    main()

