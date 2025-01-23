-- Lập danh sách các học sinh nữ
select last_name, first_name, gender
from students
where gender = 1;

-- Lập danh sách các học sinh sinh tại Osaka, Nhật Bản
select last_name, first_name, birth_place
from students
where birth_place = 'Osaka, Japan';

-- Lập danh sách các học sinh sinh tại Nhật Bản
select last_name, first_name, birth_place
from students
where birth_place like '%Japan';

-- Lập danh sách các học sinh 
select last_name, first_name, birth_date
from students
where extract(month from birth_date) = 11 or extract(month from birth_date) = 12;

-- Lập danh sách các học sinh mang họ Tào và họ Tư Mã
-- Sắp xếp họ theo thứ tự Z-A (giảm dần) và tên theo thứ tự A-Z (tăng dần)
select last_name, first_name, birth_date
from students
where last_name = 'Tào' or last_name = 'Tư Mã'
order by last_name DESC, first_name;
