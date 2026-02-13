-- Trích xuất toàn bộ dữ liệu trong bảng students
select *
from students;

-- Trích xuất 10 mẫu tin đầu tiên trong bảng students
select *
from students
limit 10;

-- Trích xuất các mẫu tin từ vị trí 3 đến 7 trong bảng students
select *
from students
limit 5
offset 3;

-- Trích xuất mã lớp, họ và tên học sinh
select classroom_id, last_name, first_name
from students;