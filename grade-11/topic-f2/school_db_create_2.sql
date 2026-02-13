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