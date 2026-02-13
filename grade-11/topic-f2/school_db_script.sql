-- Tạo cơ sở dữ liệu
create database school_db;

-- Tạo bảng students
create table students (
	student_id char(6) primary key,
	last_name varchar(50),
	first_name varchar(50),
	gender smallint,
	birth_date date,
	birth_place varchar(50)
);

-- Thêm mẫu tin vô bảng students
insert into students(student_id, last_name, first_name, gender, birth_date, birth_place) 
values
	('221001', 'Tào', 'Tháo', 0, '2007-01-15', 'Osaka, Japan'),
	('231001', 'Lưu', 'Bị', 0, '2008-01-14', 'Istanbul, Turkey'),
	('241021', 'Tôn', 'Quyền', 0, '2009-02-18', 'Dublin, Ireland');

-- Tạo bảng classrooms
create table classrooms (
    classroom_id char(5) primary key,
    classroom_name varchar(50),
    room varchar(50),
    head_teacher varchar(50)
);

-- Thêm mẫu tin vô bảng classrooms
insert into classrooms 
values ('12CTo', '12 chuyên Toán', '3.14', 'Prof. Ngô Bảo Châu'),
        ('11CTi', '11 chuyên Tin', 'Fibonacci', 'Mr School'),
        ('10CSi', '10 chuyên Sinh', 'Darwin', 'Dr Black Jack');

-- Thêm thuộc tính classroom_id vô bảng students
alter table students
add column classroom_id char(5);

-- Thêm ràng buộc khóa ngoại vô bảng students để tham chiếu đến bảng classrooms
alter table students
add constraint fk_classroom_id foreign key (classroom_id)
references classrooms(classroom_id);

-- Cập nhật dữ liệu lớp cho bảng students
update students
set classroom_id = '12CTo'
where student_id = '221001';

update students
set classroom_id = '11CTi'
where student_id = '231001';

update students
set classroom_id = '10CSi'
where student_id = '241021';

-- Tạo bảng subjects
create table subjects (
    subject_id char(2) primary key,
    subject_name varchar(100),
    description text, 
    is_mandatory boolean default true 
);

-- Thêm mẫu tin vô bảng subjects
insert into subjects
values
    ('CS', 'Khoa học máy tính', 'Khoa học xử lý dữ liệu và thông tin bằng máy tính', true),
    ('PH', 'Phòng chống nghệ thuật hắc ám', 'Phương pháp và kỹ thuật hiệu quả chống lại nghệ thuật và các sinh vật hắc ám', true),
    ('MH', 'Muggle học', 'Khoa học về những người không có phép thuật', false);

-- Tạo bảng scores
create table scores (
    student_id char(6),
    subject_id char(2),
    regular_1 float,
    regular_2 float,
    regular_3 float,
    midterm float,
    final_test float,

    -- Thiết lập khóa chính tổng hợp
    primary key (student_id, subject_id),

    -- Thiết lập khóa ngoại thứ nhất để tham chiếu đến bảng students
    foreign key (student_id) references students(student_id),

    -- Thiết lập khóa ngoại thứ hai để tham chiếu đến bảng subjects
    foreign key (subject_id) references subjects(subject_id)
);

-- Thêm mẫu tin vô bảng scores
insert into scores
values
    ('221001', 'CS', 9.2, 9.4, 8.3, 9.1, 8.5),
    ('221001', 'PH', 7.1, 9.2, 8.8, 8.2, 8.8),
    ('221001', 'MH', 9.2, 9.3, 10, 9.5, 9.3),
    ('231001', 'CS', 8.3, 8.5, 9.2, 8.5, 10),
    ('231001', 'PH', 8.6, 6.5, 7.3, 9.2, 9.5),
    ('231001', 'MH', 7.5, 7.7, 8.6, 8.5, 7.8),
    ('241021', 'CS', 9.2, 9.7, 9.3, 9.4, 7.5),
    ('241021', 'PH', 8.2, 8, 7.2, 8.5, 7.8),
    ('241021', 'MH', 10, 9.5, 9.3, 7.2, 9);

-- Bổ sung thêm nhiều mẫu tin hơn vô bảng students và scores

-- Thêm mẫu tin vô bảng students
insert into students
values
	('221002', 'Tư Mã', 'Ý', 0, '2007-02-11', 'Seoul, South Korea', '12CTo'),
	('220003', 'Tào', 'Phi', 0, '2007-03-20', 'Berlin, Germany', '12CTo'),
	('220004', 'Tào', 'Nhân', 0, '2007-04-18', 'Paris, France', '12CTo'),
	('220005', 'Tào', 'Hồng', 0, '2007-05-23', 'Amsterdam, Netherlands', '12CTo'),
	('220007', 'Bàng', 'Đức', 0, '2007-07-07', 'Istanbul, Turkey', '12CTo'),
	('220008', 'Điển', 'Vi', 0, '2007-08-30', 'Tokyo, Japan', '12CTo'),
	('220010', 'Hạ Hầu', 'Đôn', 0, '2007-10-19', 'Sydney, Australia', '12CTo'),
	('220011', 'Hạ Hầu', 'Uyên', 0, '2007-11-22', 'Dublin, Ireland', '12CTo'),
	('220012', 'Hứa', 'Chử', 0, '2007-12-01', 'Prague, Czech Republic', '12CTo'),
	('220013', 'Lý', 'Điển', 0, '2007-01-09', 'Zurich, Switzerland', '12CTo'),
	('220017', 'Quách', 'Gia', 0, '2007-05-08', 'Osaka, Japan', '12CTo'),
	('220018', 'Tuân', 'Du', 0, '2007-06-21', 'Bangkok, Thailand', '12CTo'),
	('220019', 'Tuân', 'Úc', 0, '2007-07-14', 'Buenos Aires, Argentina', '12CTo'),
	('220020', 'Trình', 'Dục', 0, '2007-08-09', 'Madrid, Spain', '12CTo'),
	('220021', 'Trương', 'Cáp', 0, '2007-09-05', 'Lisbon, Portugal', '12CTo'),
	('220022', 'Trương', 'Liêu', 0, '2007-10-27', 'Helsinki, Finland', '12CTo'),
	('220023', 'Từ', 'Hoảng', 0, '2007-11-14', 'Istanbul, Turkey', '12CTo'),
 	('220029', 'Điêu', 'Thuyền', 0, '2007-05-11', 'Madrid, Spain', '12CTo'),
	('220030', 'Tào', 'Chương', 0, '2007-06-15', 'Lisbon, Portugal', '12CTo'),
	('221031', 'Tư Mã', 'Chiêu', 0, '2007-07-19', 'Helsinki, Finland', '12CTo'),
	('220032', 'Tư Mã', 'Sư', 0, '2007-08-26', 'Istanbul, Turkey', '12CTo'),
	('221033', 'Tư Mã', 'Viêm', 0, '2007-09-13', 'Vienna, Austria', '12CTo'),
	('220034', 'Vu', 'Cấm', 0, '2007-10-22', 'Warsaw, Poland', '12CTo'),
	('221035', 'Chung', 'Hội', 0, '2007-11-16', 'Osaka, Japan', '12CTo'),
	('221036', 'Đặng', 'Ngải', 0, '2007-12-30', 'Bangkok, Thailand', '12CTo'),	
	('230002', 'Quan', 'Vũ', 0, '2008-02-19', 'Osaka, Japan', '11CTi'),
	('230003', 'Trương', 'Phi', 0, '2008-03-21', 'Copenhagen, Denmark', '11CTi'),
	('231004', 'Triệu', 'Vân', 0, '2008-04-15', 'Manila, Philippines', '11CTi'),
	('231005', 'Gia Cát', 'Lượng', 0, '2008-05-18', 'Jakarta, Indonesia', '11CTi'),
	('230006', 'My', 'Trúc', 0, '2008-06-24', 'Lisbon, Portugal', '11CTi'),
	('230007', 'Tôn', 'Càn', 0, '2008-07-27', 'Brisbane, Australia', '11CTi'),
	('231008', 'Hoàng Nguyệt', 'Anh', 1, '2008-08-13', 'Abu Dhabi, United Arab Emirates', '11CTi'),
	('230009', 'Từ', 'Thứ', 0, '2008-09-09', 'Stockholm, Sweden', '11CTi'),
	('230010', 'Hoàng', 'Trung', 0, '2008-10-06', 'Athens, Greece', '11CTi'),
	('230011', 'Ngụy', 'Diên', 0, '2008-11-02', 'Lima, Peru', '11CTi'),
	('231012', 'Bàng', 'Thống', 0, '2008-12-25', 'Kuala Lumpur, Malaysia', '11CTi'),
	('230013', 'Pháp', 'Chính', 0, '2008-01-11', 'Istanbul, Turkey', '11CTi'),
	('230014', 'Mã', 'Siêu', 0, '2008-02-07', 'Abuja, Nigeria', '11CTi'),
	('230015', 'Tưởng', 'Uyển', 0, '2008-03-30', 'New Delhi, India', '11CTi'),
	('230016', 'Vương', 'Bình', 0, '2008-04-20', 'Melbourne, Australia', '11CTi'),
	('230017', 'Lưu', 'Thiện', 0, '2008-05-29', 'Nairobi, Kenya', '11CTi'),
	('231018', 'Khương', 'Duy', 0, '2008-06-16', 'Toronto, Canada', '11CTi'),
	('230019', 'Hạ Hầu', 'Bá', 0, '2008-07-08', 'Singapore, Singapore', '11CTi'),	
	('240020', 'Tôn', 'Kiên', 0, '2009-01-12', 'Bangkok, Thailand', '10CSi'),
	('240022', 'Tôn', 'Sách', 0, '2009-03-22', 'Jakarta, Indonesia', '10CSi'),
	('240024', 'Trình', 'Phổ', 0, '2009-05-19', 'Lisbon, Portugal', '10CSi'),
	('240025', 'Từ', 'Thịnh', 0, '2009-06-27', 'Cape Town, South Africa', '10CSi'),
	('240026', 'Trương', 'Hoành', 0, '2009-07-07', 'Casablanca, Morocco', '10CSi'),
	('240027', 'Hoàng', 'Cái', 0, '2009-08-16', 'Toronto, Canada', '10CSi'),
	('240028', 'Lã', 'Mông', 0, '2009-09-09', 'Melbourne, Australia', '10CSi'),
	('240030', 'Lăng', 'Thống', 0, '2009-11-05', 'Brussels, Belgium', '10CSi'),
	('241031', 'Lỗ', 'Túc', 0, '2009-12-12', 'Stockholm, Sweden', '10CSi'),
	('241033', 'Lục', 'Tốn', 0, '2009-02-22', 'Abuja, Nigeria', '10CSi'),
	('240035', 'Thái Sử', 'Từ', 0, '2009-04-19', 'New Delhi, India', '10CSi'),
	('240036', 'Trương', 'Chiêu', 0, '2009-05-28', 'Reykjavik, Iceland', '10CSi'),
	('240037', 'Cam', 'Ninh', 0, '2009-06-16', 'Lima, Peru', '10CSi'),
	('241038', 'Chu', 'Du', 0, '2009-07-29', 'Manila, Philippines', '10CSi'),
	('240040', 'Đại', 'Kiều', 1, '2009-09-18', 'Sydney, Australia', '10CSi'),
	('240041', 'Tiểu', 'Kiều', 1, '2009-10-27', 'Dublin, Ireland', '10CSi'),
	('240043', 'Gia Cát', 'Cẩn', 0, '2009-12-30', 'Oslo, Norway', '10CSi'),
	('240045', 'Hám', 'Trạch', 0, '2009-02-23', 'Vancouver, Canada', '10CSi'),
	('240046', 'Hàn', 'Đương', 0, '2009-03-11', 'Santiago, Chile', '10CSi'),
	('240047', 'Tôn Thượng', 'Hương', 1, '2009-08-19', 'Nairobi, Kenya', '10CSi');

-- Thêm mẫu tin vô bảng scores
insert into scores
values
	('221002', 'CS', 6.6, 9.2, 9.6, 8.2, 8.9),
	('221002', 'PH', 6.4, 8.7, 4.9, 4.5, 4.9),
	('221002', 'MH', 7.9, 8.5, 6.6, 10.0, 7.2),
	('220029', 'CS', 8.8, 8.6, 5.6, 8.6, 8.1),
	('220029', 'PH', 9.7, 8.6, 7.7, 5.8, 6.7),
	('220029', 'MH', 7.0, 6.2, 6.8, 7.0, 9.2),
	('220008', 'CS', 9.2, 5.5, 7.6, 4.1, 5.0),
	('220008', 'PH', 6.4, 9.3, 6.8, 4.5, 8.7),
	('220008', 'MH', 7.7, 6.8, 5.5, 4.4, 4.7),
	('221036', 'CS', 9.7, 8.7, 8.6, 8.7, 9.5),
	('221036', 'PH', 7.0, 6.3, 9.4, 8.6, 6.1),
	('221036', 'MH', 8.3, 5.5, 5.6, 4.5, 8.5),
	('231018', 'CS', 9.8, 4.1, 8.8, 6.5, 8.3),
	('231018', 'PH', 4.5, 9.1, 8.5, 4.8, 5.3),
	('231018', 'MH', 7.2, 4.1, 6.0, 4.3, 8.4),
	('231005', 'CS', 8.4, 7.7, 5.3, 6.8, 8.8),
	('231005', 'PH', 6.0, 7.1, 8.8, 6.2, 4.5),
	('231005', 'MH', 7.3, 7.5, 5.9, 9.4, 6.2),
	('230003', 'CS', 5.5, 9.5, 5.0, 7.7, 6.2),
	('230003', 'PH', 6.5, 9.9, 9.8, 5.3, 7.4),
	('230003', 'MH', 4.3, 5.3, 6.4, 9.5, 8.5),
	('241038', 'CS', 4.6, 7.2, 4.2, 9.4, 8.1),
	('241038', 'PH', 4.5, 6.0, 4.8, 6.7, 8.8),
	('241038', 'MH', 9.2, 6.8, 7.2, 8.2, 8.4),
	('240041', 'CS', 6.0, 8.7, 9.5, 6.8, 5.5),
	('240041', 'PH', 7.7, 9.9, 9.7, 6.2, 5.2),
	('240041', 'MH', 7.7, 6.8, 8.5, 8.2, 5.2);