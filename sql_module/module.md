SELECT * FROM module_table;


SELECT
CASE
WHEN gender = 'm' THEN 'This is '|| name ||', he has email  ' || email
WHEN gender = 'f' THEN 'This is '|| name ||', she has email ' || email
END info
FROM module_table;

SELECT
CASE
WHEN gender = 'm' THEN 'We have '|| COUNT(*) ||' boys!'
WHEN gender = 'f' THEN 'We have '|| COUNT(*) ||' girls!'
END "Gender information"
FROM module_table 
GROUP BY gender;


SELECT v.name, COUNT(*) AS words
FROM vocabulary AS v
INNER JOIN word AS w
ON w.vocabulary_id = v.id
GROUP BY v.name;
