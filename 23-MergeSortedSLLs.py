# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list
# is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# works, slow- ~9.92nd percentile for runtime, ~67.3rd for memory
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []: return None
        lists_len = len(lists)
        to_pop = []
        for li in range(lists_len): # find empty lists
            if lists[li] == None: to_pop.append(li)
        minus = 0
        for tp in to_pop:   # remove empty lists
            lists.pop(tp - minus)
            minus += 1
        if lists == []: return None
        ret_head = ListNode(None)
        curr = ret_head
        lists_len = len(lists)
        while lists != []:  # add successive min values to return list
            min_val = [lists[0].val, 0]
            for li in range(len(lists)):    # find next min value
                if lists[li].val < min_val[0]:
                    min_val = [lists[li].val, li]
            curr.val = min_val[0]
            lists[min_val[1]] = lists[min_val[1]].next
            if lists[min_val[1]] == None:
                lists.pop(min_val[1])
                lists_len -= 1
            if lists != []:
                curr.next = ListNode(None)
                curr = curr.next
        return ret_head
