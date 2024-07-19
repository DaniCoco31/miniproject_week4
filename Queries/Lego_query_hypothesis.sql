USE legodb;

-- Number of Sets per Theme
-- Query:
SELECT themes.name AS Theme, COUNT(*) AS "Number of sets"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY COUNT(*) DESC
LIMIT 10;

--  Top 10 Sets with the Most Parts
-- Query:
SELECT name, num_parts
FROM sets
ORDER BY num_parts DESC
LIMIT 10;

-- Themes with the Most Parts
-- Query:
SELECT themes.name AS Theme, SUM(num_parts) AS "Total amount of parts for the theme"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY SUM(num_parts) DESC
LIMIT 10;

-- Quantity of pieces in the Oldest Sets
-- Query:
SELECT name, year, num_parts
FROM sets
WHERE year = (SELECT MIN(year) FROM sets)
ORDER BY num_parts DESC
LIMIT 10;

-- Hypothesis 1: Changes in the quantity of pieces in LEGO sets from 1950 until 2017
-- Query:
SELECT year, FLOOR(AVG(num_parts)) AS avg_num_parts
FROM sets
GROUP BY year
ORDER BY year ASC;

-- Hypothesis 2: Variation in Number of Parts Over Time
--Query:
SELECT year, MAX(num_parts) - MIN(num_parts) AS part_range
FROM sets
GROUP BY year
ORDER BY year ASC;

-- Hypothesis 3: Most Common Color in Sets
-- Query:
SELECT colors.name AS Color, COUNT(*) AS count
FROM colors
JOIN inventory_parts ON colors.id = inventory_parts.color_id
GROUP BY colors.name
ORDER BY count DESC
LIMIT 10;