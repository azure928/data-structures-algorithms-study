# LL: Find Middle Node ( \*\* Interview Question)

Implement the find_middle_node method for the LinkedList class.

The `find_middle_node` method should return the middle node in the linked list **WITHOUT** using the `length` attribute.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

- The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

- The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

- The method should only traverse the linked list once. In other words, you can only use one loop.

## Pseudo Code:

INITIALIZE slow and fast pointers to head of the linked list

WHILE fast is not None and fast.next is not None: MOVE slow pointer one step (slow = slow.next) MOVE fast pointer two steps (fast = fast.next.next)

RETURN slow pointer (middle node of the linked list)
