"""
Given k sorted singly linked lists,
write a function to merge all the lists into one sorted singly linked list.
"""


import heapq


def merge_k_sorted_linked_lists(linked_lists):
    heap = [(head.val, i, head) for i, head in enumerate(linked_list)
            if head is not None]
    heapq.heapify(heap)
    tail = dummy_head = ListNode(None)
    while heap:
        val, index, head = heapq.heappop(heap)
        tail.next = ListNode(head)
        tail = tail.next
        head = head.next
        if head:
            heapq.heappush(heap, (head.val, index, head))
    return dummy_head.next
