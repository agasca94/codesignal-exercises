# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#
def removeKFromList(l, k):
    node = l
    while node:
        if node.next and node.next.value == k:
            node.next = node.next.next
        else:
            node = node.next
    
    return l.next if l and l.value == k else l