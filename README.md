Data Analysis Project Plan: Analyzing LEGO Sets Data
Project Title: Analyzing Trends and Complexity in LEGO Sets

Objective: To analyze various aspects of LEGO sets, including the number of sets per theme, the complexity of sets over time, and the evolution of LEGO set components. The goal is to derive insights that can aid in strategic decision-making for product development, marketing, and inventory management.

Data Source: LEGO database consisting of the following tables:

colors
inventories
inventory_parts
inventory_sets
part_categories
parts
sets
themes
Hypotheses and Queries
Hypothesis 1: Number of Sets per Theme
Relevance: Understanding the popularity of different themes helps identify key areas of interest for customers. This can guide future theme development and marketing strategies.

Query:

SELECT themes.name AS Theme, COUNT(*) AS "Number of sets"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY COUNT(*) DESC
LIMIT 10;

mportance for Decision Making: This analysis highlights the most popular themes, enabling better allocation of resources and marketing efforts towards high-demand themes.

Hypothesis 2: Top 10 Sets with the Most Parts
Relevance: Identifying the sets with the most parts can provide insights into the most complex and potentially most engaging sets for enthusiasts.

Query:
SELECT name, num_parts
FROM sets
ORDER BY num_parts DESC
LIMIT 10;

Importance for Decision Making: This information can help in promoting high-complexity sets to advanced builders and collectors, tailoring marketing campaigns to target these audiences.

Hypothesis 3: Top 10 Sets with the Least Parts
Relevance: Knowing which sets have the fewest parts helps in identifying simpler sets that may appeal to younger children or beginners.

Query:

SELECT name, num_parts
FROM sets
WHERE num_parts >= 1
ORDER BY num_parts ASC
LIMIT 10;

Importance for Decision Making: This can inform the development of entry-level sets and educational products, making LEGO more accessible to new customers.

Hypothesis 4: Themes with the Most Parts
Relevance: Analyzing themes with the most parts can indicate which themes offer the most complex building experiences.

Query:

SELECT themes.name AS Theme, SUM(num_parts) AS "Total amount of parts for the theme"
FROM themes
LEFT JOIN sets ON themes.id = sets.theme_id
GROUP BY themes.name
ORDER BY SUM(num_parts) DESC
LIMIT 10;

Importance for Decision Making: Understanding which themes are associated with high-part counts can guide product development towards themes that demand more intricate designs.

Hypothesis 5: Quantity of Pieces in the Oldest Sets
Relevance: Examining the oldest sets helps understand the evolution of LEGO set complexity and the brand's historical product offerings.

Query:
SELECT name, year, num_parts
FROM sets
WHERE year = (SELECT MIN(year) FROM sets)
ORDER BY num_parts DESC
LIMIT 10;

Importance for Decision Making: This historical insight can be used for nostalgic marketing campaigns and to showcase the brand's heritage.

Hypothesis 6: Changes in the Quantity of Pieces in LEGO Sets from 1950 Until 2017
Relevance: Analyzing changes in the average number of pieces over time provides insights into how set complexity has evolved, reflecting changing consumer preferences and technological advancements.

Query:

SELECT year, FLOOR(AVG(num_parts)) AS avg_num_parts
FROM sets
GROUP BY year
ORDER BY year ASC;

Importance for Decision Making: This trend analysis can guide future product development strategies, ensuring that new sets align with evolving consumer expectations for complexity and engagement.

Implementation Plan
Data Collection and Preparation:

Extract data from the LEGO database.
Ensure data integrity and consistency across tables.
Data Analysis:

Execute the provided SQL queries to analyze each hypothesis.
Use visualization tools (e.g., Tableau, Power BI) to create charts and graphs for better interpretation of results.
Insight Generation:

Interpret the results of the queries to derive actionable insights.
Identify trends and patterns that can inform strategic decisions.
Reporting:

Compile findings into a comprehensive report.
Present the insights using visual aids to stakeholders.
Decision Making:

Use the insights to inform product development, marketing strategies, and inventory management.
Develop recommendations for future projects based on the data analysis.
Conclusion
This project plan outlines the steps needed to analyze the LEGO sets data effectively. By investigating the provided hypotheses, we aim to gain valuable insights into the evolution and complexity of LEGO sets. These insights will support strategic decision-making processes and help guide the future direction of LEGO products and marketing efforts.


