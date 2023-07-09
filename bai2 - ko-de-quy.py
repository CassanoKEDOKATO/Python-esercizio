class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def Xoa_Node_Ko_De_Quy(head, key):
    if head is None:
        return head
    if head.data == key:
        return head.next
    current = head          # tạo node current gán bằng node đầu
    while current.next:     #duyệt node current đến cuối
        if current.next.data == key:   
            current.next = current.next.next  # nhảy tới node sau node cần xoá
            return head
        current = current.next

    return head

# Tạo danh sách nối đơn
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth

# Xoá nút có giá trị 3 trong danh sách
head = Xoa_Node_Ko_De_Quy(head, 3)

# In danh sách sau khi xoá
current = head
while current:
    print(current.data)
    current = current.next