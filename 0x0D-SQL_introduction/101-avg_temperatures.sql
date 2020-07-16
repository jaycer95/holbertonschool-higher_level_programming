-- Display the average temperature
SELECT city, avg(value) as avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg(value) DESC;
