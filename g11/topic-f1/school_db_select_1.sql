-- Liệt kê toàn bộ dữ liệu trong bảng students
select *
from students;

-- Liệt kê 10 mẫu tin đầu tiên trong bảng students
select *
from students
limit 10;

-- Liệt kê các mẫu tin từ 11 đến 15 trong bảng students
select *
from students
limit 5
offset 10;

-- Liệt kê lớp và họ tên học sinh
select classroom_id, last_name, first_name
from students;