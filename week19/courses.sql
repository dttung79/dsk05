-- Xóa nếu đã tồn tại
DROP TABLE IF EXISTS Prerequisite;
DROP TABLE IF EXISTS Course;

-- 1. Bảng Course: danh sách các môn học
CREATE TABLE Course (
  CourseID    INT         PRIMARY KEY,
  CourseName  VARCHAR(100) NOT NULL,
  Credits     INT         NOT NULL
);

-- 2. Bảng Prerequisite: mỗi dòng ghép một quan hệ "Course cần PrereqCourse"
CREATE TABLE Prerequisite (
  CourseID        INT NOT NULL,
  PrereqCourseID  INT NOT NULL,
  PRIMARY KEY (CourseID, PrereqCourseID),
  FOREIGN KEY (CourseID)       REFERENCES Course(CourseID),
  FOREIGN KEY (PrereqCourseID) REFERENCES Course(CourseID)
);

-- 3. Chèn dữ liệu vào Course
INSERT INTO Course (CourseID, CourseName, Credits) VALUES
  (101, 'Intro to Programming',    3),
  (102, 'Data Structures',         4),
  (103, 'Algorithms',              4),
  (104, 'Databases',               3),
  (105, 'Operating Systems',       4),
  (106, 'Computer Networks',       3),
  (107, 'Software Engineering',    3),
  (201, 'Linear Algebra',          3),
  (202, 'Calculus',                3),
  (203, 'Statistics',              3),
  (204, 'Machine Learning',        4);

-- 4. Chèn dữ liệu vào Prerequisite
INSERT INTO Prerequisite (CourseID, PrereqCourseID) VALUES
  (102, 101),  -- Data Structures ← Intro
  (103, 102),  -- Algorithms      ← Data Structures
  (104, 102),  -- Databases       ← Data Structures
  (105, 102),  -- OS              ← Data Structures
  (106, 102),  -- Networks        ← Data Structures
  (107, 102),  -- SE              ← Data Structures
  (204, 103),  -- ML              ← Algorithms
  (204, 201),  -- ML              ← Linear Algebra
  (204, 203);  -- ML              ← Statistics