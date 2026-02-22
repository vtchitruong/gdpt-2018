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

-- Thêm mẫu tin vào bảng students
insert into students(student_id, last_name, first_name, gender, birth_date, birth_place) 
values
	('220001', 'Tào', 'Tháo', 0, '2007-01-15', 'Osaka, Japan'),
	('230001', 'Lưu', 'Bị', 0, '2008-01-14', 'Istanbul, Turkey'),
	('240021', 'Tôn', 'Quyền', 0, '2009-02-18', 'Dublin, Ireland');

-- Tạo bảng classrooms
create table classrooms (
    classroom_id char(5) primary key,
    classroom_name varchar(50),
    room varchar(50),
    head_teacher varchar(50)
);

-- Thêm mẫu tin vào bảng classrooms
insert into classrooms 
values ('12CTo', '12 chuyên Toán', '3.14', 'Prof. Ngô Bảo Châu'),
        ('11CTi', '11 chuyên Tin', 'Fibonacci', 'Mr School'),
        ('10CSi', '10 chuyên Sinh', 'Darwin', 'Dr Black Jack');

-- Thêm thuộc tính classroom_id vào bảng students
alter table students
add column classroom_id char(5);

-- Tạo ràng buộc khoá ngoại từ students tham chiếu đến classrooms
alter table students
add constraint fk_classroom_id foreign key (classroom_id) 
references classrooms(classroom_id);

-- Cập nhật dữ liệu lớp cho bảng students
update students
set classroom_id = '12CTo'
where student_id = '220001';

update students
set classroom_id = '11CTi'
where student_id = '230001';

update students
set classroom_id = '10CSi'
where student_id = '240021';