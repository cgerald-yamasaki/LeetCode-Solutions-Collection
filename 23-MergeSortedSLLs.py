# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list
# is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# deals with duplicates all at once rather than in successive big loops
# possibly optimal runtime, with 55.6th percentile for memory
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
            min_val = lists[0].val
            mins_to_add = []
            for li in range(len(lists)):    # find next min value
                if lists[li].val < min_val:
                    min_val = lists[li].val
                    mins_to_add = [li]
                elif lists[li].val == min_val:
                    mins_to_add.append(li)
            minus = 0
            for m in mins_to_add:
                curr.val = min_val
                lists[m - minus] = lists[m - minus].next
                if lists[m - minus] == None:
                    lists.pop(m - minus)
                    lists_len -= 1
                    minus += 1
                if lists != []:
                    curr.next = ListNode(None)
                    curr = curr.next
        return ret_head

# Moved stuff around, -> even slower
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if lists == []: return None
#         lists_len = len(lists)
#         ret_head = ListNode(None)
#         curr = ret_head
#         lists_len = len(lists)
#         while lists != []:  # add successive min values to return list
#             while lists != [] and lists[0] == None: # remove leading empty lists
#                 lists.pop(0)
#                 lists_len -= 1
#             if lists == []: return None
#             min_val = [lists[0].val, 0]
#             to_pop = []
#             for li in range(lists_len):    # find next min value
#                 if lists[li] == None:
#                     to_pop.append(li)
#                     continue
#                 if lists[li].val < min_val[0]:
#                     min_val = [lists[li].val, li]
#             curr.val = min_val[0]
#             lists[min_val[1]] = lists[min_val[1]].next
#             if lists[min_val[1]] == None:
#                 to_pop.append(min_val[1])
#             tp_count = 0
#             for tp in to_pop:
#                 lists.pop(tp - tp_count)
#                 tp_count += 1
#                 lists_len -= 1
#             if lists != []:
#                 curr.next = ListNode(None)
#                 curr = curr.next
#         if ret_head.val == None: return None
#         return ret_head

# works, slow- ~9.92nd percentile for runtime, ~67.3rd for memory
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if lists == []: return None
#         lists_len = len(lists)
#         to_pop = []
#         for li in range(lists_len): # find empty lists
#             if lists[li] == None: to_pop.append(li)
#         minus = 0
#         for tp in to_pop:   # remove empty lists
#             lists.pop(tp - minus)
#             minus += 1
#         if lists == []: return None
#         ret_head = ListNode(None)
#         curr = ret_head
#         lists_len = len(lists)
#         while lists != []:  # add successive min values to return list
#             min_val = [lists[0].val, 0]
#             for li in range(len(lists)):    # find next min value
#                 if lists[li].val < min_val[0]:
#                     min_val = [lists[li].val, li]
#             curr.val = min_val[0]
#             lists[min_val[1]] = lists[min_val[1]].next
#             if lists[min_val[1]] == None:
#                 lists.pop(min_val[1])
#                 lists_len -= 1
#             if lists != []:
#                 curr.next = ListNode(None)
#                 curr = curr.next
#         return ret_head
