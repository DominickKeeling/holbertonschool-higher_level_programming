-- Select the required fields with a condition on the score and order by score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
