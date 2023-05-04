-- we select the [total number of fans by origin
-- lets know the origin of our fas
SELECT origin, SUM(fans) AS nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
