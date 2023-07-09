a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

for i in range(k):
    # Lưu giá trị của phần tử đầu tiên vào biến temp
    temp = a[0]
    
    # Dịch chuyển tất cả các phần tử sang trái
    for j in range(len(a)-1):
        a[j] = a[j+1]
    
    # Gán giá trị của biến temp vào vị trí cuối cùng của mảng
    a[-1] = temp

print(a)   # Output: [4, 5, 6, 7, 8, 1, 2, 3]