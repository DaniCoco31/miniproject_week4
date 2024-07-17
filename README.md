



Hypohtesis


how many sets are there for themes

-- how many sets are there for themes
SELECT themes.name AS Theme, count(*) AS "Number of sets"
FROM themes 
LEFT JOIN sets
on themes.id = sets.theme_id
group by themes.name
order by count(*) DESC
limit 10


average of pieces per theme
the 10 sets with more pieces
the 10 sets with less pieces
how many pieces had the first 10 sets of legos
how many pieces had the last 10 sets of legos
whis is the most common color of the pieces


