# Cờ Vây AI 9X9

- Go 9x9 AI Web App là một ứng dụng web mô phỏng trò chơi Cờ Vây (Go) 9x9, được xây dựng với mục tiêu kết hợp giữa lập trình web hiện đại và trí tuệ nhân tạo (AI) nhằm tái hiện một môi trường thi đấu chiến thuật thông minh, trực quan và đầy tính tương tác. Dự án được phát triển trên nền tảng Flask bằng ngôn ngữ Python, kết hợp cùng giao diện HTML, CSS và JavaScript để mang đến trải nghiệm mượt mà, thân thiện và dễ tiếp cận cho người dùng.
- Điểm nổi bật của ứng dụng nằm ở hệ thống AI chơi cờ tự động, được thiết kế dựa trên các thuật toán tìm kiếm và ra quyết định nổi tiếng như Minimax, Alpha-Beta Pruning và Heuristic Evaluation. Nhờ đó, AI có khả năng phân tích trạng thái bàn cờ theo thời gian thực, đánh giá lợi thế chiến thuật giữa hai bên, dự đoán các kịch bản tiếp theo và lựa chọn những nước đi tối ưu nhất. Điều này không chỉ giúp tăng tính cạnh tranh trong trò chơi mà còn mô phỏng rõ nét cách một hệ thống trí tuệ nhân tạo “tư duy” và đưa ra quyết định trong môi trường có nhiều biến số.
- Không đơn thuần là một trò chơi giải trí, Go 9x9 AI Web App còn là một dự án mang tính học thuật và thực tiễn cao, thể hiện sự giao thoa giữa khoa học máy tính, thuật toán, và tư duy chiến lược. Ứng dụng giúp người dùng hiểu rõ hơn về cách AI vận hành trong các bài toán tối ưu, đồng thời tạo ra một nền tảng trực quan để sinh viên, nhà phát triển hoặc những người yêu thích công nghệ có thể khám phá và nghiên cứu sâu hơn về lĩnh vực Artificial Intelligence thông qua một bài toán kinh điển của trí tuệ nhân loại: Cờ Vây.
- Với bàn cờ 9x9 nhỏ gọn nhưng đầy thách thức, dự án không chỉ tái hiện tinh thần chiến thuật đặc trưng của môn cờ cổ truyền hàng nghìn năm tuổi này, mà còn minh chứng cho tiềm năng ứng dụng mạnh mẽ của AI trong việc giải quyết các bài toán chiến lược phức tạp trong thế giới hiện đại. Go 9x9 AI Web App chính là nơi công nghệ gặp gỡ tư duy, nơi mỗi nước cờ không chỉ là một lựa chọn — mà còn là kết quả của hàng loạt phép tính và chiến lược được AI phân tích phía sau.


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



## Link Trải Nghiệm Game

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
