-- Trích xuất họ, tên, lớp học và phòng học của các học sinh
select last_name, first_name, classroom_name, room
from students
inner join classrooms on students.classroom_id = classrooms.classroom_id;

-- Dùng USING
select last_name, first_name, classroom_name, room
from students
inner join classrooms using(classroom_id);

-- Trích xuất họ, tên, mã lớp học, tên lớp học và phòng học của các học sinh
select last_name, first_name, students.classroom_id, classroom_name, room
from students
inner join classrooms using(classroom_id);

-- Trích xuất họ, tên, tên môn học và điểm thi cuối kỳ của các học sinh trong môn Khoa học máy tính
select last_name, first_name, subject_name, final_test
from scores
inner join subjects on scores.subject_id = subjects.subject_id
inner join students on scores.student_id = students.student_id
where subject_name = 'Khoa học máy tính';

-- Dùng USING
select last_name, first_name, subject_name, final_test
from scores
inner join subjects using(subject_id)
inner join students using(student_id)
where subject_name = 'Khoa học máy tính';