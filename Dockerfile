# Dùng image python chính thức, phiên bản 3.10 slim nhẹ
FROM python:3.10-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt ./

# Cài các thư viện python
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code của bạn vào container
COPY . .

# Lệnh chạy ứng dụng (thay main.py bằng file chính của bạn)
CMD ["python", "main.py"]
