-- Display the top 3 of cities temperature during July and August 
SELECT city, avg(value) as avg_temp 
FROM temperatures
WHERE MONTH=7 or MONTH=8
GROUP BY city
ORDER BY avg(value) DESC
LIMIT 3;