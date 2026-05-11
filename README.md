# Go 9x9 AI Web App

Một ứng dụng web mô phỏng trò chơi **C[object Object]ờ Vây 9x9**, được xây dựng bằng **Python Flask**, kết hợp giao diện **HTML/CSS/JavaScript** và tích hợp AI có khả năng tự động đưa ra nước đi dựa trên thuật toán **Minimax**, **Alpha-Beta Pruning** và **Heuristic Evaluation**.

Ứng dụng hướng đến mục tiêu minh họa cách AI có thể phân tích trạng thái bàn cờ, đánh giá lợi thế và lựa chọn nước đi phù hợp trong phạm vi bàn cờ 9x9.

---
## Alpha-Beta Pruning 
---
Alpha-Beta Pruning là kỹ thuật tối ưu của thuật toán Minimax trong AI chơi game đối kháng như:
- Cờ Vây 9x9 
- Cờ vua 
-	Cờ caro 
- Othello 
-	Tic Tac Toe 
Nó giúp AI:
- tìm nước đi tốt hơn nhanh hơn, 
- giảm số trạng thái cần xét, 
- tăng độ sâu suy nghĩ mà không tốn quá nhiều thời gian. 
Alpha-Beta dựa trên:
- Lý thuyết trò chơi (Game Theory) 
- Tìm kiếm cây trạng thái (Game Tree Search) 
- Nguyên lý Minimax 
Trong game đối kháng 2 người:
- Một bên cố gắng tối đa hóa lợi ích → MAX 
- Một bên cố gắng giảm lợi ích đối thủ → MIN



## Demo

Trải nghiệm trực tiếp tại:

[Go 9x9 AI Web App](https://c-vay-n.onrender.com/)

---

## Tính năng chính

- Giao diện chơi cờ vây 9x9 trực quan trên web
- Người chơi có thể thi đấu trực tiếp với AI
- Bàn cờ được vẽ bằng HTML Canvas, giúp thao tác click mượt hơn
- AI tự động phân tích bàn cờ và đưa ra nước đi
- AI sử dụng thuật toán Minimax để tìm nước đi phù hợp
- Tối ưu tốc độ tìm kiếm bằng Alpha-Beta Pruning
- Đánh giá trạng thái bàn cờ bằng Heuristic Evaluation
- Có hệ thống tính điểm giữa người chơi và AI
- Hiển thị kết quả thắng, thua hoặc hòa khi ván cờ kết thúc
- Có thể triển khai online để người dùng bấm link và chơi trực tiếp

---

## Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Xử lý logic trò chơi và thuật toán AI |
| Flask | Xây dựng backend web và API xử lý lượt chơi |
| HTML | Xây dựng cấu trúc giao diện web |
| CSS | Thiết kế giao diện, màu sắc và bố cục |
| JavaScript | Xử lý thao tác click, cập nhật bàn cờ và gọi API |
| Canvas API | Vẽ bàn cờ và quân cờ trên trình duyệt |
| Minimax Algorithm | Thuật toán giúp AI lựa chọn nước đi |
| Alpha-Beta Pruning | Tối ưu quá trình tìm kiếm nước đi |
| Heuristic Evaluation | Đánh giá độ tốt của trạng thái bàn cờ |

---

## Cài đặt và chạy local

### 1. Cài đặt thư viện

bash
pip install -r requirements.txt

### 2. Chạy ứng dụng
python app.py
## 3. Bảng Phân Công Công Việc Chi Tiết
| STT | Họ và Tên | MSSV | Vai trò | Chi tiết công việc |
|---|---|---|---|---|
| 1 | Nguyễn Anh Quốc | 233009 | Leader / Backend / Dev AI | - Khởi tạo source base cho dự án GibHub. <br> - Xây dựng cấu trúc chính của ứng dụng trong `app.py`. <br> - Kết nối giao diện, logic game và AI <br> - Tạo logic cho AI. <br> - Quản lý tiến độ, kiểm tra và tổng hợp source code. |
| 2 | Trầm Quốc Hùng | 233044 | Dev AI / Backend / Report | - Xây dựng logic cho AI <br> Tăng độ nhận biết AI <br> - Chuẩn bị bài báo cáo trước khi thuyết trình .|
| 3 | Trần Khai Nguyễn | 232749 | Frontend / UI Developer/Tester | -Thiết kế giao diện wed bằng html , css , js , python, Hiển thị bàn cờ , Quân cờ , Trạng thái.<br> - Xây dựng các nút chức năng Chơi Lại , Kết Thúc Tính Điểm <br> - Tối Ưu wed hiệu ứng tăng trải nghiệm chơi cờ vây. |
| 4 | Huỳnh Hoàng Khang | 232583 | Dev AI / Backend | - Xậy dựng hệ thống AI , xây dựng logic cho AI <br> - Tối ứu hóa AI làm AI mượt hơn  . |
| 5 | Ngô hữu Danh | 232818 | Tester / Document / Support | - Kiểm thử toàn bộ chức năng của ứng dụng. <br> - Phát hiện lỗi trong quá trình chơi và đề xuất chỉnh sửa. <br> - Viết file `README.md` hướng dẫn cài đặt, chạy local và demo. <br> - Hỗ trợ triển khai ứng dụng lên Streamlit Community Cloud.  |
| 6 | nguyễn Hoàng Thông | 232676 | Deploy / Support/ Thuyết Trình | - Kiểm tra cấu trúc source code trước khi nộp. <br> - Hỗ trợ deploy ứng dụng lên Dashboard render. <br> - Kiểm tra link demo và đảm bảo app chạy ổn định trên web./ Thuyết Trình   |
