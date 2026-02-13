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