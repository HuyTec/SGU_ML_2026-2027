# LAB 01: PyTorch Basics

Các bài được tổ chức thành 3 nhóm để giảm số lượng file nhưng vẫn giữ đủ nội dung:

1. `01_tensor_basics.py`: tạo tensor, thuộc tính, indexing, slicing, reshape, phép toán, thống kê, chuyển đổi và device.
2. `02_autograd_optimization.py`: autograd, gradient descent cho đa thức và giải hệ phương trình bằng autograd.
3. `03_practice.py`: bài tập tổng hợp.

Các nội dung tensor được gom vào một file vì đều là kiến thức nền tảng. Autograd và các bài tối ưu được gom vào một file vì dùng chung cơ chế gradient. Các file đã gộp trước đó đều đang rỗng nên không có mã nguồn bị mất.
# 1. Mục Tiêu
## Sau khi hoàn thành bài thực hành, sinh viên có thể:
- Tạo, kiểm tra và thao tác với Tensor trong PyTorch.

- Thực hiện indexing, slicing, reshape và các phép toán ma trận trên Tensor.

- Sử dụng các hàm thống kê cơ bản trên Tensor.

- Hiểu cơ chế automatic differentiation (autograd) và vai trò của gradient.

- Sử dụng optimizer để giải bài toán tối ưu đơn giản bằng Gradient Descent.

- PyTorch cung cấp hai khả năng nền tảng: tính toán Tensor (tương tự NumPy, có thể tăng tốc bằng GPU) và automatic differentiation để huấn luyện mô hình.