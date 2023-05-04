-- we use the iFNULL and Now function
-- lets get the lifespan
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%GLAM rock%'
ORDER BY lifespan DESC;
