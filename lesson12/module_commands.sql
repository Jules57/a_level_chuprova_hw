1 task

INSERT INTO module_table
VALUES
(1, 'Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),  
(2, 'Alex', '21341234', 'mmm@gmail.com', 'm'),
(3, 'Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
(4, 'Helen', 'MarryMeee', 'hell@gmail.com', 'f'),
(5, 'Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
(6, 'Lora', 'burn23', 'tpicks@gmail.com', 'f');


2 task

SELECT 
CASE
WHEN gender = 'm' THEN 'This is '|| name ||', he has email  ' || email
WHEN gender = 'f' THEN 'This is '|| name ||', she has email ' || email
END info
FROM module_table;


3 task
SELECT 
'We have ' || COUNT(*) || ' boys!' 
AS "Gender information"
FROM module_table
WHERE gender = 'm'
UNION
SELECT
'We have ' || COUNT(*) || ' girls!' 
FROM module_table
WHERE gender = 'f';

4 task

SELECT v.name, COUNT(*) AS words 
FROM vocabulary AS v
INNER JOIN word AS w 
ON w.vocabulary_id = v.id 
GROUP BY v.name
ORDER BY v.name;
