-- Lập danh sách học sinh, kèm theo lớp và phòng học
select last_name, first_name, classroom_name, room
from students inner join classrooms on students.classroom_id = classrooms.classroom_id;

-- Lập danh sách học sinh, kèm theo mã lớp, tên lớp và phòng học
select last_name, first_name, students.classroom_id, classroom_name, room
from students inner join classrooms on students.classroom_id = classrooms.classroom_id;

-- In ra bảng điểm môn Khoa học máy tính của tất cả học sinh
select last_name, first_name, subject_name, final_test
from scores inner join subjects on scores.subject_id = subjects.subject_id
            inner join students on scores.student_id = students.student_id
where subject_name = 'Khoa học máy tính';
