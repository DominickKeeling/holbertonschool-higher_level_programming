-- select all records of the second table table of the database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
