-- Cho biết huyết thống lai (half-blood) là huyết thống như thế nào
select blood_name, blood_description
from bloods
where lower(blood_name) = 'half-blood';

-- Cho biết họ tên đầy đủ của người sáng lập nhà Slytherin và hai màu sắc đặc trưng của nhà này (color_1, color_2)
select house_name, founder, color_1, color_2
from houses
where house_name = 'Slytherin';

-- Đọc câu thần chú (incantation) có tác dụng (effect) triệu hồi đồ vật (Summons an object)
select incantation, effect
from spells
where effect = 'Summons an object';

-- Cách khác
select incantation, effect
from spells
where effect like 'Summons an object%';

-- Liệt kê các môn học bắt buộc (regular) trong trường Hogwarts
-- Sắp xếp tên môn học (subject_name) theo thứ tự bảng chữ cái
select subject_name, subject_type
from subjects
where lower(subject_type) = 'regular'
order by subject_name;

-- Cho biết những chủng loại nào có liên quan đến loài người (human)
select spec_name, spec_description
from species
where spec_description ilike '%human%';

-- Cách khác
select spec_name, spec_description
from species
where spec_description ~~* '%human%';

-- Cho biết năng lực (skills) của các thành viên gia đình Potter (last_name là Potter)
-- Sắp xếp tăng dần theo họ (last_name), nếu trùng họ thì sắp xếp giảm dần theo tên (first_name)
select first_name, last_name, skills
from characters
where last_name ilike 'weasley%'
order by last_name, first_name desc;
