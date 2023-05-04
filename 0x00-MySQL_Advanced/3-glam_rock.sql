-- we use the iFNULL and Now function
-- lets get the lifespan
SELECT band_name, (IFNULL(split, YEAR(NOW())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%GLAM rock%';
