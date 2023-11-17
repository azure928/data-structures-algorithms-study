# LL: Has Loop ( \*\* Interview Question)

Write a method called `has_loop` that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:

1. Create two pointers, `slow` and `fast`, both initially pointing to the head of the linked list.

2. Traverse the list with the `slow` pointer moving one step at a time, while the `fast` pointer moves two steps at a time.

3. If there is a loop in the list, the `fast` pointer will eventually meet the `slow` pointer. If this occurs, the method should return `True`.

4. If the `fast` pointer reaches the end of the list or encounters a `None` value, it means there is no loop in the list. In this case, the method should return `False`.

## Pseudo Code:

initialize slow and fast pointers to head of the list

while fast is not None and fast.next is not None:

    move slow pointer one step forward

    move fast pointer two steps forward



    if slow and fast pointers are equal:

        return True (loop found)

return False (loop not found)
