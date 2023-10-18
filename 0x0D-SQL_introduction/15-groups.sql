-- Ascript that lists number of records with same score
SELECT scor, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;

