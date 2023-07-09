def chuyen_k_phan_tu_cuoi_mang(a, k):
    left = a[:k]
    right = a[k:]
    # Chuyển k phần tử đầu tiên về cuối mảng
    a = right + left
    return a

# Kiểm tra đoạn code
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
a = chuyen_k_phan_tu_cuoi_mang(a, k)
print(a)