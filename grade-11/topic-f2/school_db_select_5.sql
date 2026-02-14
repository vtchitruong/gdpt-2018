-- Đếm số lượng mẫu tin trong bảng scores
select count(*) as "Số lượng"
from scores;

-- Đếm số lượng điểm cuối kỳ từ 5 trở lên tính chung các môn
select count(*) as "Số lượng"
from scores
where final_test >= 5;

-- Đếm số lượng điểm cuối kỳ từ 5 trở lên theo từng môn
select subject_id, count(*) as "Số lượng"
from scores
where final_test >= 5
group by subject_id;

-- Đếm số lượng điểm cuối kỳ từ 5 trở lên theo từng môn, chỉ lấy môn nào có số lượng học sinh lớn hơn 10
select subject_id, count(*) as "Số lượng"
from scores
where final_test >= 5
group by subject_id
having count(*) > 10;