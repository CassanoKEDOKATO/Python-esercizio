class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def DeleteNodeRecursive(head, key):
    if head is None:     
        return head
    if head.data == key:     
        return head.next
    head.next = DeleteNodeRecursive(head.next, key)  
    return head


head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth

# Xoá nút có giá trị 3 trong danh sách
head = DeleteNodeRecursive(head, 3)

# In danh sách sau khi xoá
current = head
while current:
    print(current.data)
    current = current.next