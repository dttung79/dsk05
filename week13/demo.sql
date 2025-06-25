use abc;
CREATE TABLE Employees (
	EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(100),
    Salary DECIMAL(10, 2),
    HireDate DATE
);

INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) 
VALUES (1, 'Angela Wade', 'HR', 2485.28, '2014-10-11');

INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (2, 'Kenneth Lopez', 'Marketing', 1973.47, '2013-01-11');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (3, 'Susan Walker', 'Engineering', 4000.0, '2011-05-06');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (4, 'Mark Martinez', 'Engineering', 2864.77, '2020-12-27');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (5, 'Angela Barnes', 'Engineering', 1637.13, '2014-08-20');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (6, 'William Garcia', 'Marketing', 1637.13, '2011-03-01');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (7, 'Dustin Roberts', 'Engineering', 500.0, '2016-03-04');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (8, 'Lisa Smith', 'Engineering', 2120.62, '2011-08-14');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (9, 'Melissa Wilson', 'HR', 1764.77, '2016-11-11');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (10, 'Melissa Smith', 'Engineering', 2225.88, '2015-06-28');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (11, 'Amanda Kennedy', 'HR', 500.0, '2014-10-30');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (12, 'Michael Mccoy', 'Engineering', 1735.71, '2016-09-02');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (13, 'Jeffrey Jones', 'Marketing', 2686.59, '2015-03-31');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (14, 'Jeffrey Taylor', 'Marketing', 2448.2, '2018-05-26');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (15, 'Erica Lowe', 'HR', 2093.17, '2011-06-10');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (16, 'Christopher Lopez', 'Engineering', 2282.39, '2019-09-24');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (17, 'James Green', 'Engineering', 500.0, '2014-06-28');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (18, 'Shawn Mccann', 'Marketing', 2214.47, '2012-11-09');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (19, 'Jason Hill', 'Marketing', 1976.58, '2013-06-09');
INSERT INTO Employees (EmployeeID, Name, Department, Salary, HireDate) VALUES (20, 'Brandon Henry', 'HR', 2182.92, '2012-03-24');


-- Lọc bảng lấy 2 cột Name và Salary
SELECT Name, Salary
FROM Employees;

-- Lọc tất cả các cột, lấy nhân viên của phòng HR
SELECT *
FROM Employees
WHERE Department = 'HR';

-- Lọc tất cả các cột, lấy nhân viên của phòng HR có lương hơn 2000
SELECT *
FROM Employees
WHERE Department = 'HR' AND Salary >= 2000;

-- Lọc tất cả các cột, lấy nhân viên của phòng HR hoặc Marketing
SELECT *
FROM Employees
WHERE Department = 'HR' OR Department = 'Marketing';

-- Lọc nhân viên có lương trong khoảng 1000 và 2000
SELECT *
FROM Employees
WHERE Salary BETWEEN 1000 and 2000;

-- Lọc nhân viên có lương trong khoảng 1000 và 2000 và sắp sếp lương tăng dần
SELECT *
FROM Employees
WHERE Salary BETWEEN 1000 and 2000
ORDER BY Salary ASC;

-- Lọc nhân viên có lương trong khoảng 1000 và 2000 và sắp sếp tăng dần theo tên
SELECT *
FROM Employees
WHERE Salary BETWEEN 1000 and 2000
ORDER BY Name DESC;

-- Lọc nhân viên có lương trong khoảng 1000 và 2000 và sắp sếp tăng dần theo tên, giới hạn 3 kết quả
SELECT *
FROM Employees
WHERE Salary BETWEEN 1000 and 2000
ORDER BY Name DESC
LIMIT 3;

-- Lọc dữ liệu không trùng lặp
SELECT DISTINCT Department
FROM Employees;

-- Tính tổng lương của từng phòng ban
SELECT Department, SUM(SALARY) As TotalSalary
FROM Employees
GROUP BY Department;

-- Tính trung bình lương của từng phòng ban
SELECT Department, AVG(SALARY) As AverageSalary
FROM Employees
GROUP BY Department;

-- Đếm xem mỗi phòng ban có bao nhiêu nhân viên
SELECT Department, COUNT(*) As NumberOfEmployees
FROM Employees
GROUP BY Department;

-- Đếm số nhân viên có lương >= 2000 của mỗi phòng ban
select department, count(employeeid) as total_emp
from employees
where salary > 2000
group by department;


-- THỰC HÀNH VỚI BẢNG SALES
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    Product VARCHAR(50),
    Salesperson VARCHAR(50),
    SaleDate DATE,
    Quantity INT,
    Price DECIMAL(10, 2),
    Total DECIMAL(10, 2)
);

-- Thêm dữ liệu mẫu
INSERT INTO Sales (SaleID, Product, Salesperson, SaleDate, Quantity, Price, Total) VALUES
(1, 'Laptop', 'Alice', '2024-01-15', 2, 1000, 2000),
(2, 'Laptop', 'Bob', '2024-02-20', 1, 1000, 1000),
(3, 'Monitor', 'Alice', '2024-03-10', 5, 200, 1000),
(4, 'Keyboard', 'Charlie', '2024-01-25', 10, 50, 500),
(5, 'Laptop', 'Alice', '2024-02-05', 3, 1000, 3000),
(6, 'Monitor', 'Bob', '2024-03-20', 2, 200, 400),
(7, 'Keyboard', 'Alice', '2024-03-15', 4, 50, 200),
(8, 'Mouse', 'Alice', '2024-03-22', 6, 30, 180),
(9, 'Laptop', 'Charlie', '2024-02-28', 2, 950, 1900),
(10, 'Monitor', 'Alice', '2024-01-18', 3, 210, 630),
(11, 'Mouse', 'Bob', '2024-03-01', 10, 25, 250),
(12, 'Keyboard', 'Charlie', '2024-02-12', 5, 60, 300);


-- Tính tổng doanh thu
SELECT SUM(Total) AS TotalRevenue
FROM Sales;

-- Lọc sản phẩm Laptop
SELECT * 
FROM SALES
WHERE Product = 'Laptop';

-- Tính tổng doanh thu Laptop theo từng nhân viên
SELECT Salesperson, SUM(Total) as Total_Revernue
FROM Sales
WHERE Product = 'Laptop'
group by Salesperson;

-- Tính tổng số lượng sản phẩm bán ra theo từng sản phẩm
SELECT Product, SUM(Quantity) AS TotalQuantity
FROM Sales
GROUP BY Product;

-- Tính doanh thu trung bình theo nhân viên
SELECT Salesperson, AVG(Total) as AvgTotal
FROM sales
GROUP BY Salesperson;

-- Đếm tổng số lượng của từng sản phẩm và sắp xếp tăng dần (theo sản phẩm)
select product, sum(quantity) as so_luong_sp
from sales
group by product
order by product asc;

-- Lọc ra những nhân viên có tổng doanh thu trên 2000
SELECT Salesperson, SUM(Total) AS TotalRevenue
FROM Sales
GROUP BY Salesperson
HAVING SUM(Total) > 2000;

-- Lọc ra những sản phẩm có số lượng bán trung bình > 5
select product, avg(quantity) as so_luong_sp
from sales
group by product
having avg(quantity) > 5;

-- Tìm các ngày có doanh thu > 1000
select saledate, sum(total) as total_date
from sales
group by saledate
having sum(total) > 1000;