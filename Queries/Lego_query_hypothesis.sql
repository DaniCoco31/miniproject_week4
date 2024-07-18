USE legodb;

-- Hypothesis 1: Number of Sets per Theme
-- Query:
SELECT themes.name AS Theme, COUNT(*) AS "Number of sets"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY COUNT(*) DESC
LIMIT 10;

-- Hypothesis 2: Top 10 Sets with the Most Parts
-- Query:
SELECT name, num_parts
FROM sets
ORDER BY num_parts DESC
LIMIT 10;

-- Hypothesis 3: Top 10 Sets with the Least Parts
-- Query:
SELECT name, num_parts
FROM sets
WHERE num_parts >= 1
ORDER BY num_parts ASC
LIMIT 10;

-- Hypothesis 4: Themes with the Most Parts
-- Query:
SELECT themes.name AS Theme, SUM(num_parts) AS "Total amount of parts for the theme"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY SUM(num_parts) DESC
LIMIT 10;

-- Hypothesis 5: Quantity of pieces in the Oldest Sets
-- Query:
SELECT name, year, num_parts
FROM sets
WHERE year = (SELECT MIN(year) FROM sets)
ORDER BY num_parts DESC
LIMIT 10;

-- Hypothesis 6: Changes in the quantity of pieces in LEGO sets from 1950 until 2017
-- Query:
SELECT year, FLOOR(AVG(num_parts)) AS avg_num_parts
FROM sets
GROUP BY year
ORDER BY year ASC;