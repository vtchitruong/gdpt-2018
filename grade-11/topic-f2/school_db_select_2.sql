-- Trích xuất họ và tên của các học sinh có giới tính là nữ
select last_name, first_name, gender
from students
where gender = 1;

-- Trích xuất họ và tên của các học sinh có nơi sinh là Osaka, Japan
select last_name, first_name, birth_place
from students
where birth_place = 'Osaka, Japan';

-- Trích xuất họ và tên của các học sinh có nơi sinh là Japan
select last_name, first_name, birth_place
from students
where birth_place like '%Japan';

-- Trích xuất họ và tên của các học sinh có tháng sinh là 11 hoặc 12
select last_name, first_name, birth_date
from students
where extract(month from birth_date) = 11 or extract(month from birth_date) = 12;