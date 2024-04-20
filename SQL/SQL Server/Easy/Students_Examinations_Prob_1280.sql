
--Write a solution to find the number of times each student attended each exam.

--Return the result table ordered by student_id and subject_name.


select T1.student_id, T1.student_name, T1.subject_name subject_name, ISNULL(T2.attended_exams, 0) attended_exams
from (select distinct * from Students, Subjects
group by student_id, student_name, subject_name) T1 left join  (select student_id, subject_name, count(subject_name) attended_exams from Examinations
group by student_id, subject_name) T2
on T1.student_id = T2.student_id
and T1.subject_name = T2.subject_name
group by T1.student_id, T1.student_name, T1.subject_name, T2.attended_exams
order by T1.student_id


Select S.student_id,S.student_name,Subjects.subject_name,count(E.subject_name) as attended_exams From Students S
cross join Subjects
left  join Examinations E on S.student_id = E.student_id And Subjects.subject_name = E.subject_name group by S.student_id,S.student_name,Subjects.subject_name
