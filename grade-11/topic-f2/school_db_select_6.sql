-- Tính giá trị trung bình của cột điểm cuối kỳ theo từng môn
select subject_name, avg(final_test) as "Điểm trung bình"
from scores
inner join subjects using(subject_id)
group by subject_name;

-- Tính giá trị trung bình của cột điểm cuối kỳ cho riêng môn Khoa học máy tính
select subject_name, avg(final_test) as "Điểm trung bình"
from scores
inner join subjects using(subject_id)
where subject_name = 'Khoa học máy tính'
group by subject_name;

-- Lọc ra các môn mà giá trị trung bình của cột điểm cuối kỳ lớn hơn 7
select subject_name, avg(final_test) as "Điểm trung bình"
from scores
inner join subjects using(subject_id)
group by subject_name
having avg(final_test) > 7;