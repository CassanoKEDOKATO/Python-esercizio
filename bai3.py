def find_max_diff(a):
    n = len(a)
    max_diff = float('-inf')   #tạo giá trị âm
    
    for i in range(n):
        for j in range(i+1, n):
            max_diff = max(max_diff, a[j] - a[i])
    
    return max_diff
    
a = [5,8,6,7,1,3,6]
print(find_max_diff(a))