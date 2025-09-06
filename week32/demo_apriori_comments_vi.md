# Giải thích chi tiết từng cell — `week32/demo_apriori.ipynb`

Lưu ý: Các dòng bắt đầu bằng dấu `#` dưới đây là chú thích (comment) bằng tiếng Việt giải thích mục đích của từng cell và các câu lệnh chính bên trong.

## Cell 0
- Import thư viện:
  - `pandas`, `numpy`: xử lý dữ liệu.
  - `apyori.apriori`: thuật toán Apriori để khai phá luật kết hợp.

Mục tiêu: Chuẩn bị công cụ cần để đọc dữ liệu và khai thác luật.

## Cell 1
- Đọc file Excel `Online Retail.xlsx` vào DataFrame `df`.

Mục tiêu: Nạp dữ liệu giao dịch bán lẻ.

## Cell 2
- Lấy 5000 dòng đầu tiên để demo, giúp chạy nhanh và gọn.

Mục tiêu: Giảm kích thước dữ liệu cho bài minh họa.

## Cell 3
- `df.head(10)`: xem nhanh 10 dòng đầu để hình dung cấu trúc dữ liệu.

Mục tiêu: Khảo sát sơ bộ dữ liệu.

## Cell 4
- `df.dtypes`: kiểm tra kiểu dữ liệu các cột (số, chuỗi, thời gian, ...).

Mục tiêu: Đảm bảo kiểu dữ liệu phù hợp trước xử lý.

## Cell 5
- `df.describe()`: thống kê mô tả cơ bản cho các cột số (min, max, mean, ...).

Mục tiêu: Nắm đặc trưng tổng quan của dữ liệu số.

## Cell 6
- `df['StockCode'].nunique()`: đếm số mã hàng (sản phẩm) khác nhau.

Mục tiêu: Biết độ đa dạng sản phẩm.

## Cell 7
- Nhóm theo `StockCode`, cộng `Quantity`, sắp xếp giảm dần và lấy top 10.
- In ra các sản phẩm bán chạy (tổng số lượng).

Mục tiêu: Khám phá sản phẩm bán chạy nhất.

## Cell 8
- Ép kiểu `InvoiceNo`, `StockCode` thành chuỗi và thêm khoảng trắng ở cuối.

Lý do: Ở bước sau, khi biểu diễn từng hóa đơn là danh sách item, việc có khoảng trắng đảm bảo mã giống nhau có định dạng nhất quán (tránh dính ký tự khi ghép/hiển thị).

## Cell 9
- Khởi tạo danh sách `transactions` rỗng.
- Lấy danh sách các hóa đơn duy nhất `invoices` từ cột `InvoiceNo`.

Mục tiêu: Chuẩn bị tạo tập giao dịch cho thuật toán Apriori.

## Cell 10
- In số lượng hóa đơn (số giao dịch) trong tập con 5000 dòng.

Mục tiêu: Kiểm tra kích thước tập giao dịch.

## Cell 11
- Duyệt từng `iv` (mã hóa đơn) trong `invoices`:
  - Lọc `df` theo hóa đơn đó, lấy danh sách sản phẩm `StockCode`.
  - Thêm danh sách item này vào `transactions`.
- In tổng số giao dịch thu được.

Mục tiêu: Biến dữ liệu dạng bảng thành danh sách các giỏ hàng (transactions) cho Apriori.

## Cell 12
- In ra 5 giao dịch đầu tiên để kiểm tra cấu trúc dữ liệu `transactions`.

Mục tiêu: Xác nhận định dạng đầu vào trước khi chạy Apriori.

## Cell 13
- Gọi hàm `apriori` với các tham số:
  - `min_support=0.02`: luật phải xuất hiện trong ít nhất 2% giao dịch.
  - `min_confidence=0.3`: độ tin cậy tối thiểu 30%.
  - `min_lift=3`: độ nâng tối thiểu 3 (mạnh hơn ngẫu nhiên 3 lần).
  - `max_length=2`: tập mục (itemset) tối đa 2 phần tử.

Mục tiêu: Khai phá các tập phổ biến và luật kết hợp theo ngưỡng.

## Cell 14
- Ép kết quả sinh ra (iterator) thành danh sách.
- In số lượng luật/tập phổ biến thu được.

Mục tiêu: Lưu trữ kết quả để dễ duyệt/in.

## Cell 15
- Duyệt 5 kết quả đầu tiên `rule`:
  - `rule.items`: tập item phổ biến.
  - `rule.support`: độ hỗ trợ của tập item.
  - `rule.ordered_statistics`: các luật suy ra từ tập đó, gồm:
    - `items_base` (vế trái), `items_add` (vế phải)
    - `confidence`, `lift`

Mục tiêu: In chi tiết các luật đầu tiên để quan sát chất lượng.

## Cell 16
- Sắp xếp kết quả theo `support` giảm dần, in top 5 tương tự cell 15.

Mục tiêu: Xem các tập mục phổ biến nhất (theo hỗ trợ).

## Cell 17
- Chọn 2 mã sản phẩm `code1`, `code2` cần kiểm tra đồng xuất hiện.
- Duyệt các `rule` và in ra những luật/tập chứa cả 2 mã đó, kèm `support`, các `ordered_statistics` liên quan và chỉ số `confidence`, `lift`.

Mục tiêu: Truy vấn thủ công các luật liên quan tới cặp sản phẩm cụ thể.

