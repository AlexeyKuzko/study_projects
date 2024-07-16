SELECT AVG(s.age) AS average_age
FROM students s
JOIN enrollments e ON s.id = e.student_id
WHERE e.course_id = 2024;