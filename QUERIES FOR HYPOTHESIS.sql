#Number of sets per theme

SELECT themes.name AS Theme, count(*) AS "Number of sets"
FROM themes
LEFT JOIN sets
on themes.id = sets.theme_id
group by themes.name
order by count(*) DESC
limit 10;

#Top 10 sets with the most parts

select name, num_parts
from sets
order by num_parts desc
limit 10;

#Top 10 sets with the least parts

select name, num_parts
from sets
where num_parts >= 1
order by num_parts asc
limit 10;

#Which themes usually have the most parts?
SELECT themes.name AS Theme, sum(num_parts) as "Total amount of parts for the theme"
FROM themes
LEFT JOIN sets
on themes.id = sets.theme_id
group by themes.name
order by sum(num_parts) desc;

#how many pieces had the oldest sets in the database?
select name,  year, num_parts
from sets
where year = (select min(year) from sets);

#how many pieces have the newest sets in the database?

select name,  year, num_parts
from sets
where year = (select max(year) from sets);

#Most common color



#IGNORE
select name, count(*) as "Times repeated"
from colors
group by name

select sets.name, colors.name
from sets
join inventories
on sets.set_num = inventories.set_num
join inventory_parts
on inventory_parts.inventory_id = inventories.id
join colors
on inventory_parts.color_id = colors.id