# Go 9x9 AI Web App

Một ứng dụng web mô phỏng trò chơi **Cờ Vây 9x9** được xây dựng bằng **Python Streamlit**, tích hợp AI có khả năng tự động đưa ra nước đi dựa trên thuật toán **Minimax**, **Alpha-Beta Pruning** và **Heuristic Evaluation**.

Ứng dụng hướng đến mục tiêu minh họa cách AI có thể phân tích trạng thái bàn cờ, đánh giá lợi thế và lựa chọn nước đi tối ưu trong phạm vi bàn cờ 9x9.

---

## Demo

Trải nghiệm trực tiếp tại:

[Go 9x9 AI Web App](https://covayne.streamlit.app/)

---

## Tính năng chính

- Giao diện chơi cờ vây 9x9 trực quan trên web
- Người chơi có thể thi đấu với AI
- AI sử dụng thuật toán Minimax để tìm nước đi phù hợp
- Tối ưu tốc độ tìm kiếm bằng Alpha-Beta Pruning
- Đánh giá thế cờ bằng Heuristic Evaluation
- Hỗ trợ chạy trực tiếp trên trình duyệt thông qua Streamlit
- Có thể triển khai nhanh trên Streamlit Community Cloud

---

## Công nghệ sử dụng

- **Python** – xử lý logic trò chơi và thuật toán AI
- **Streamlit** – xây dựng giao diện web tương tác
- **Minimax Algorithm** – thuật toán ra quyết định cho AI
- **Alpha-Beta Pruning** – tối ưu quá trình tìm kiếm nước đi
- **Heuristic Evaluation** – đánh giá chất lượng trạng thái bàn cờ

---

## Cài đặt và chạy local

### 1. Cài đặt thư viện
pip install -r requirements.txt
### 2. Chạy ứng dụng
streamlit run app.py
## 3. Bảng Phân Công Công Việc Chi Tiết
| STT | Họ và Tên | MSSV | Vai trò | Chi tiết công việc |
|---|---|---|---|---|
| 1 | Nguyễn Anh Quốc | 233009 | Leader / Backend | - Khởi tạo source base cho dự án Streamlit. <br> - Xây dựng cấu trúc chính của ứng dụng trong `app.py`. <br> - Kết nối giao diện, logic game và AI. <br> - Quản lý tiến độ, kiểm tra và tổng hợp source code. |
| 2 | Trầm Quốc Hùng | 233044 | Dev AI / Backend | - Xây dựng thuật toán Minimax cho AI. <br> - Tích hợp Alpha-Beta Pruning để tối ưu tốc độ tìm kiếm. <br> - Thiết kế hàm Heuristic Evaluation để đánh giá trạng thái bàn cờ. <br> - Kiểm thử khả năng ra quyết định của AI. |
| 3 | Trần Khai Nguyễn | 232749 | Game Logic Developer | - Xây dựng logic bàn cờ 9x9. <br> - Xử lý luật đặt quân và kiểm tra nước đi hợp lệ. <br> - Cập nhật trạng thái bàn cờ sau mỗi lượt chơi. <br> - Xử lý điều kiện kết thúc ván cờ và tính điểm cơ bản. |
| 4 | Huỳnh Hoàng Khang | 232583 | Frontend / UI Developer | - Thiết kế giao diện web bằng Streamlit. <br> - Hiển thị bàn cờ, quân cờ và trạng thái lượt chơi. <br> - Xây dựng các nút chức năng như Play Again, End & Score. <br> - Tối ưu trải nghiệm người dùng khi thao tác trên web. |
| 5 | Ngô hữu Danh | 232818 | Tester / Document | - Kiểm thử toàn bộ chức năng của ứng dụng. <br> - Phát hiện lỗi trong quá trình chơi và đề xuất chỉnh sửa. <br> - Viết file `README.md` hướng dẫn cài đặt, chạy local và demo. <br> - Hỗ trợ triển khai ứng dụng lên Streamlit Community Cloud. |
| 6 | nguyễn Hoàng Thông | 232676 | Deploy / Support / Report | - Kiểm tra cấu trúc source code trước khi nộp. <br> - Hỗ trợ deploy ứng dụng lên Streamlit Community Cloud. <br> - Kiểm tra link demo và đảm bảo app chạy ổn định trên web. <br> - Tổng hợp nội dung báo cáo, chỉnh sửa format README và hỗ trợ chuẩn bị thuyết trình. |
