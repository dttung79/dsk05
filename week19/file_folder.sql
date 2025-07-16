-- Xóa nếu đã tồn tại
DROP TABLE IF EXISTS File;
DROP TABLE IF EXISTS Folder;

-- 1. Bảng Folder (mỗi folder có thể nằm trong 1 parent folder, NULL nếu là root folder)
CREATE TABLE Folder (
    FolderID        INT            PRIMARY KEY,
    FolderName      VARCHAR(100)   NOT NULL,
    ParentFolderID  INT            NULL,
    CreatedDate     DATE           NOT NULL,
    FOREIGN KEY (ParentFolderID) REFERENCES Folder(FolderID)
);

-- 2. Bảng File (mỗi file nằm trong 1 folder)
CREATE TABLE File (
    FileID       INT            PRIMARY KEY,
    FileName     VARCHAR(255)   NOT NULL,
    FolderID     INT            NOT NULL,
    SizeKB       INT            NOT NULL,      
    CreatedDate  DATE           NOT NULL,
    FOREIGN KEY (FolderID) REFERENCES Folder(FolderID)
);

-- 3. Chèn dữ liệu mẫu cho Folder
INSERT INTO Folder (FolderID, FolderName, ParentFolderID, CreatedDate) VALUES
  (1, 'root',        NULL,      '2020-01-01'),
  (2, 'Documents',   1,         '2020-02-10'),
  (3, 'Images',      1,         '2020-02-12'),
  (4, 'Work',        2,         '2020-03-15'),
  (5, 'Personal',    2,         '2020-04-01'),
  (6, 'Vacation',    3,         '2021-06-20'),
  (7, 'Projects',    4,         '2021-01-05'),
  (8, 'Archive',     1,         '2022-01-01');

-- 4. Chèn dữ liệu mẫu cho File
INSERT INTO File (FileID, FileName, FolderID, SizeKB, CreatedDate) VALUES
  ( 1, 'resume.pdf',       2,   120,   '2020-02-15'),
  ( 2, 'budget.xlsx',      4,   256,   '2020-03-20'),
  ( 3, 'family.jpg',       3,  1024,   '2020-02-20'),
  ( 4, 'project1.docx',    7,   512,   '2021-01-10'),
  ( 5, 'vacation1.jpg',    6,  2048,   '2021-06-25'),
  ( 6, 'vacation2.png',    6,  3072,   '2021-06-26'),
  ( 7, 'secret.txt',       5,     1,   '2020-04-02'),
  ( 8, 'archive.zip',      8, 10240,   '2022-02-01'),
  ( 9, 'notes.txt',        1,     2,   '2022-05-10'),
  (10, 'diagram.svg',      4,   750,   '2020-03-17');