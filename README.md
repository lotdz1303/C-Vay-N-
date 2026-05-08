# Go 9x9 AI Web App

Một ứng dụng web mô phỏng trò chơi **Cờ Vây 9x9** được xây dựng bằng **Python Streamlit**, tích hợp AI có khả năng tự động đưa ra nước đi dựa trên thuật toán **Minimax**, **Alpha-Beta Pruning** và **Heuristic Evaluation**.

Ứng dụng hướng đến mục tiêu minh họa cách AI có thể phân tích trạng thái bàn cờ, đánh giá lợi thế và lựa chọn nước đi tối ưu trong phạm vi bàn cờ 9x9.

---

## Demo

Trải nghiệm trực tiếp tại:

[Go 9x9 AI Web App](https://co-vay-9x9-aifix-qzxnp6cszk2jtchehu5dpp.streamlit.app/)

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

### 1. Clone repository

### 2. Cài đặt thư viện
pip install -r requirements.txt
### 3. Chạy ứng dụng
streamlit run app.py
