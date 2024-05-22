class ListNode:
    
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def reverse_linked_list(head) -> list[int]:
        values : list[int] = []
        queue : list [ListNode] = [head]

        while queue:
            current_node: ListNode = queue.pop()
            if current_node:
                values.append(current_node.val)
                queue.append(current_node.next)
        return values[::-1]