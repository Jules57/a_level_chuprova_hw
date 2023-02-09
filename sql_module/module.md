Task 1. Create table

```SELECT * FROM module_table;```

<img width="449" alt="Initial table" src="https://user-images.githubusercontent.com/90455735/217814686-49b405c1-614e-4a1c-abda-f363548d7cf7.png">

Task 2. Select names and emails from the table.

```
SELECT
CASE
WHEN gender = 'm' THEN 'This is '|| name ||', he has email  ' || email
WHEN gender = 'f' THEN 'This is '|| name ||', she has email ' || email
END info
FROM module_table;
```

<img width="520" alt="emails_by_owners" src="https://user-images.githubusercontent.com/90455735/217814747-f76a5702-5e4a-483a-aedf-0fc41c328684.png">

Task 3. Count representatives of different genders.

```
SELECT
CASE
WHEN gender = 'm' THEN 'We have '|| COUNT(*) ||' boys!'
WHEN gender = 'f' THEN 'We have '|| COUNT(*) ||' girls!'
END "Gender information"
FROM module_table 
GROUP BY gender;
```

<img width="409" alt="count_boys_and_girls" src="https://user-images.githubusercontent.com/90455735/217814851-7662b7b6-4761-4bce-834b-59ecc8ba7f82.png">


Task 5. Count words from table word.

```
SELECT v.name, COUNT(*) AS words
FROM vocabulary AS v
INNER JOIN word AS w
ON w.vocabulary_id = v.id
GROUP BY v.name;
```

<img width="365" alt="count_words" src="https://user-images.githubusercontent.com/90455735/217814892-f8d2faa0-2103-40bc-b1e4-bf6fa628f54e.png">

