-- Tính số lượng mẫu tin trong bảng scores
select count(student_id) as "Số lượng"
from scores;

-- Tính số lượng điểm cuối kỳ từ 5 trở lên ở tất cả các môn
select count(student_id) as "Số lượng"
from scores
where final_test >= 5;

-- Tính số lượng điểm cuối kỳ từ 5 trở lên theo từng môn
select subject_id, count(student_id) as "Số lượng"
from scores
where final_test >= 5
group by subject_id;

-- Tính số lượng điểm cuối kỳ từ 5 trở lên theo từng môn, chỉ lấy môn nào có số lượng hơn 10
select subject_id, count(student_id) as "Số lượng"
from scores
where final_test >= 5
group by subject_id
having count(student_id) > 10;

-- Tính giá trị trung bình của cột điểm cuối kỳ theo từng môn
-- Kết quả trả về phải có tên môn
select subject_name, avg(final_test) as "Điểm trung bình"
from scores inner join subjects on scores.subject_id = subjects.subject_id
group by subject_name;

-- Tính giá trị trung bình của cột điểm cuối kỳ cho riêng môn Khoa học máy tính
select subject_name, avg(final_test) as "Điểm trung bình"
from scores inner join subjects on scores.subject_id = subjects.subject_id
where subject_name = 'Khoa học máy tính'
group by subject_name;

-- Lọc ra các môn mà giá trị trung bình của cột điểm cuối kỳ lớn hơn 7
select subject_name, avg(final_test) as "Điểm trung bình"
from scores inner join subjects on scores.subject_id = subjects.subject_id
group by subject_name
having avg(final_test) > 7;
