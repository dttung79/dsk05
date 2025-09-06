# Giải thích chi tiết từng cell — `week32/demo_fpgrowth.ipynb`

## Cell 0
- Import thư viện:
  - `pandas`, `numpy` để xử lý dữ liệu.
  - `TransactionEncoder` để mã hóa danh sách giao dịch sang ma trận one-hot.
  - `fpgrowth`, `association_rules` từ `mlxtend.frequent_patterns` để tìm tập mục phổ biến bằng FP-Growth và sinh luật kết hợp.

## Cell 1
- Đọc `Online Retail.xlsx` và giới hạn 5000 dòng đầu để demo.

Mục tiêu: Chuẩn bị dữ liệu đầu vào gọn nhẹ.

## Cell 2
- `invoice_stockcode`: nhóm theo cặp (`InvoiceNo`, `StockCode`) và đếm số dòng (cột `Count`).

Mục tiêu: Chuẩn hóa dữ liệu ở mức “mỗi hóa đơn - mỗi sản phẩm xuất hiện 1 lần”.

## Cell 3
- In kích thước `invoice_stockcode` và xem vài dòng đầu.

Mục tiêu: Xác nhận kết quả nhóm đúng mong đợi.

## Cell 4
- `stockcode_freq`: tính số hóa đơn khác nhau mà mỗi `StockCode` xuất hiện (`nunique` trên `InvoiceNo`).
- In kích thước/đầu bảng.

Mục tiêu: Lấy tần suất xuất hiện theo số hóa đơn.

## Cell 5
- Tính tổng số hóa đơn `total_invoices`.
- Tính `Support` = `Freq` / `total_invoices` cho từng `StockCode`.
- In kích thước và xem đầu bảng.

Mục tiêu: Hỗ trợ (support) đơn lẻ của từng sản phẩm.

## Cell 6
- Sắp xếp `stockcode_freq` theo `Support` giảm dần và in top 10.

Mục tiêu: Xem các sản phẩm phổ biến nhất.

## Cell 7
- Ép `InvoiceNo`, `StockCode` thành chuỗi và thêm khoảng trắng để chuẩn hóa định dạng khi xây mảng giao dịch.

## Cell 8
- Xây danh sách `transactions`: mỗi phần tử là danh sách các `StockCode` trong một `InvoiceNo`.
- In tổng số giao dịch.

Mục tiêu: Tạo dữ liệu đầu vào cho FP-Growth.

## Cell 9
- In 5 giao dịch đầu để kiểm tra cấu trúc dữ liệu.

## Cell 10
- Dùng `TransactionEncoder` để fit và transform `transactions` thành ma trận boolean (one-hot) `t_encoded`.
- Đưa vào `DataFrame` với cột là tên item (`encoder.columns_`).
- In kích thước và xem vài dòng đầu.

Mục tiêu: Định dạng dữ liệu theo yêu cầu của `mlxtend`.

## Cell 11
- Chạy `fpgrowth` với `min_support=0.05` để tìm `frequent_itemsets` (có `use_colnames=True` để hiển thị tên cột thay vì chỉ số).
- In kích thước kết quả.

## Cell 12
- Sinh luật kết hợp `fp_rules` từ `frequent_itemsets` với tiêu chí `metric='confidence'`, ngưỡng `min_threshold=0.2`.

## Cell 13
- In số lượng luật tìm được.

## Cell 14
- Sắp xếp luật theo `confidence` giảm dần, lấy 10 luật đầu.
- Với mỗi luật: in dạng `antecedents -> consequents` kèm `support`, `confidence`, `lift` (định dạng 3 chữ số thập phân).

Mục tiêu: Trình bày các luật mạnh nhất để tham khảo.

