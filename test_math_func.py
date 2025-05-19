# Import các hàm add và divide từ module math_func
from math_func import add, divide

# Hàm kiểm thử hàm add
def test_add():
    # Kiểm tra xem add(2, 3) có cho kết quả đúng là 5 không
    assert add(2, 3) == 5

# Hàm kiểm thử hàm divide
def test_divide():
    # Kiểm tra xem divide(10, 2) có cho kết quả đúng là 5 không
    assert divide(10, 2) == 5
