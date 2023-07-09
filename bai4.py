# Để tìm độ dài dãy con tăng lớn nhất của một dãy số a, ta có thể sử dụng phương pháp Dynamic Programming với độ phức tạp thời gian O(n^2) hoặc O(n log n).

# Phương pháp Dynamic Programming:

# Bước 1: Khởi tạo một mảng dp với kích thước bằng với a, trong đó dp[i] là độ dài của dãy con tăng lớn nhất kết thúc tại vị trí i trong mảng a.

# Bước 2: Gán giá trị ban đầu cho dp bằng 1.

# Bước 3: Duyệt mảng a từ đầu đến cuối và tính giá trị tương ứng của dp[i] với công thức sau:

# for i in range(1, n):
# for j in range(i):
# if a[i] > a[j]:
# dp[i] = max(dp[i], dp[j] + 1)

# Công thức này sẽ tính giá trị của dp[i] bằng giá trị lớn nhất của dp[j] + 1 với j < i và a[j] < a[i]. Tức là nếu giá trị tại vị trí j nhỏ hơn giá trị tại vị trí i thì ta sẽ cập nhật giá trị dp[i] bằng giá trị lớn nhất của dp[j] + 1.

# Bước 4: Sau khi duyệt xong mảng, giá trị lớn nhất của dp sẽ chứa độ dài của dãy con tăng lớn nhất của mảng a.

# Sau khi hoàn thành các bước trên với mảng a={1,2,3,9,10,5,6,7,8}, ta sẽ có kết quả là 8, do dãy con tăng lớn nhất là {1,2,3,5,6,7,8,9}.
def find_longest_increasing_subsequence(a):
    n = len(a)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
    
a = [1,2,3,4,9,10,5,6,7,8]
print(find_longest_increasing_subsequence(a))