# Hàm cộng hai số
def add(x, y):
    return x + y  # Trả về tổng của x và y

# Hàm chia hai số
def divide(x, y):
    if y == 0:
        # Nếu y bằng 0 thì không thể chia, đưa ra ngoại lệ
        raise ValueError("Cannot divide by zero.")
    return x / y  # Trả về kết quả của phép chia x cho y
