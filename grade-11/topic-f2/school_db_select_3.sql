-- Trích xuất họ, tên và ngày sinh của các học sinh mang họ Tào và họ Tư Mã
-- Sắp xếp họ theo thứ tự Z-A (giảm dần) và tên theo thứ tự A-Z (tăng dần)
select last_name, first_name, birth_date
from students
where last_name = 'Tào' or last_name = 'Tư Mã'
order by last_name DESC, first_name;
