# Giải thích chi tiết từng cell — `week31/cf/demo_cf.ipynb`

Mô hình: Hệ gợi ý cộng tác (Collaborative Filtering) dựa trên độ tương đồng cosine giữa các sách (item-based), dùng ma trận xếp hạng người dùng × sách.

## Cell 0
- Import `pandas`, `numpy` để xử lý dữ liệu.

## Cell 1
- Đọc 3 file CSV: `Books.csv`, `Users.csv`, `Ratings.csv` vào 3 DataFrame tương ứng.

## Cell 2
- `books_df.head()`: xem vài dòng đầu của dữ liệu sách.

## Cell 3
- `users_df.head()`: xem vài dòng đầu của dữ liệu người dùng.

## Cell 4
- `ratings_df.head()`: xem vài dòng đầu của dữ liệu đánh giá.

## Cell 5
- In kích thước của 3 bảng (`shape`) để có cái nhìn tổng quan.

## Cell 6
- `books_df.isnull().sum()`: đếm số giá trị thiếu theo cột trong bảng sách.

## Cell 7
- `books_df.dropna(how='any', inplace=True)`: loại các dòng có thiếu dữ liệu trong bảng sách.
- Kiểm tra lại số thiếu và in kích thước sau khi làm sạch.

## Cell 8
- Kiểm tra số giá trị thiếu trong bảng người dùng.

## Cell 9
- Kiểm tra số giá trị thiếu trong bảng đánh giá.

## Cell 10
- `ratings_books_df = ratings_df.merge(books_df, on='ISBN')`: nối (inner join) đánh giá với thông tin sách theo khóa `ISBN`.

## Cell 11
- Xem một vài dòng đầu của bảng đã nối để xác nhận.

## Cell 12
- Tạo `rating_numbers_df`: đếm số bản ghi đánh giá theo `Book-Title` (số lượng đánh giá mỗi sách).

## Cell 13
- Tạo `rating_avg_df`: tính điểm trung bình `Book-Rating` theo `Book-Title`.

## Cell 14
- Đổi tên cột: số đánh giá thành `num_ratings`, điểm trung bình thành `avg_rating`.
- Gộp hai bảng trên theo `Book-Title` thành `rating_total`.

## Cell 15
- In min/max/mean của `num_ratings` để hiểu phân phối số lượng đánh giá.

## Cell 16
- In min/max/mean của `avg_rating` để hiểu phân phối điểm trung bình.

## Cell 17
- Import `matplotlib`, `seaborn` và vẽ KDE của số lượng đánh giá (unique) mỗi sách.
- Mục tiêu: Quan sát phân phối độ phổ biến của sách.

## Cell 18
- Lọc những sách có ít nhất 100 đánh giá và sắp xếp theo `avg_rating` giảm dần, xem top 10.

## Cell 19
- Nối danh sách sách phổ biến với bảng `books_df` để có thêm metadata và loại bỏ bản sao theo `Book-Title`.

## Cell 20
- Lấy top 50 sách phổ biến, in kích thước.

## Cell 21
- Xác định “expert users”: người có ≥ 200 đánh giá (`groupby('User-ID').count()['Book-Rating'] >= 200`).
- Lấy ra index (ID) của nhóm người dùng này.

## Cell 22
- Lọc các đánh giá chỉ từ nhóm user “expert”.
- Xem vài dòng đầu và kích thước.

## Cell 23
- Trong tập đánh giá của expert users, chọn các sách có ≥ 50 đánh giá để đảm bảo đủ dữ liệu.
- Lấy ra danh sách tên sách đạt điều kiện.

## Cell 24
- `final_ratings`: giữ lại các đánh giá thuộc về những sách lọc ở bước trên.
- Xem một vài dòng đầu.

## Cell 25
- In kích thước của `final_ratings`.

## Cell 26
- Tạo bảng xoay `pt`: index = `Book-Title`, columns = `User-ID`, values = `Book-Rating`.
- Đây là ma trận sách × người dùng (điểm đánh giá), dạng thưa (nhiều giá trị thiếu).

## Cell 27
- In kích thước ma trận `pt`.

## Cell 28
- Điền giá trị thiếu bằng 0 để tiện tính độ tương đồng.
- In lại kích thước (không đổi số hàng/cột, nhưng dữ liệu giờ đầy đủ số học).

## Cell 29
- Xem vài dòng đầu của ma trận đã điền 0.

## Cell 30
- Import `cosine_similarity` và tính ma trận tương đồng cosine giữa các hàng (sách) trong `pt`.
- Lưu vào `similarity_scores` và in kích thước (số sách × số sách).

## Cell 31
- Xem 5 hàng đầu của ma trận tương đồng để tham khảo.

## Cell 32
- Chọn một cuốn sách mẫu: `'Harry Potter and the Prisoner of Azkaban (Book 3)'`.
- Tìm chỉ số hàng tương ứng trong `pt.index` và in chỉ số đó.

## Cell 33
- Lấy vector tương đồng của sách đã chọn: `book_similarity = similarity_scores[book_index]`.
- In kích thước vector (số sách).

## Cell 34
- Sắp xếp sách theo độ tương đồng giảm dần, bỏ chính nó (`[1:11]` để lấy top 10 gần nhất).
- In ra danh sách (index, score) đã sắp xếp.

## Cell 35
- Duyệt các sách tương tự nhất vừa tìm và in tên (`pt.index[i[0]]`).

Ghi chú:
- Ma trận điền 0 có thể làm thiên lệch tương đồng; thay thế khác là chuẩn hóa hoặc chỉ so sánh trên người dùng chung (k-sparse). Tuy nhiên, cho demo, cách này đơn giản và đủ trực quan.
- Có thể mở rộng sang user-based CF bằng cách xoay trục hoặc tính tương đồng theo cột.

