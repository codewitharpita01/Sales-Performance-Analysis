
 1. View all records
SELECT *
FROM SalesData_Import;

 2. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM SalesData_Import;

3. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM SalesData_Import;

4. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM SalesData_Import;

5. Average Sales
SELECT AVG(Sales) AS Average_Sales
FROM SalesData_Import;

 6. Average Profit
SELECT AVG(Profit) AS Average_Profit
FROM SalesData_Import;

 7. Sales by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY Category
ORDER BY Total_Sales DESC;

 8. Profit by Category
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Category
ORDER BY Total_Profit DESC;


 9. Sales by Region
SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY Region
ORDER BY Total_Sales DESC;

 10. Profit by Region
SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Region
ORDER BY Total_Profit DESC;

11. Sales by Segment
SELECT
    Segment,
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY Segment
ORDER BY Total_Sales DESC;

 12. Profit by Segment
SELECT
    Segment,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Segment
ORDER BY Total_Profit DESC;

13. Sales by Ship Mode
SELECT
    [Ship Mode],
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY [Ship Mode]
ORDER BY Total_Sales DESC;

14. Profit by Ship Mode
SELECT
    [Ship Mode],
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY [Ship Mode]
ORDER BY Total_Profit DESC;

 15. Sales by Sub-Category
SELECT
    [Sub-Category],
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY [Sub-Category]
ORDER BY Total_Sales DESC;

 16. Profit by Sub-Category
SELECT
    [Sub-Category],
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY [Sub-Category]
ORDER BY Total_Profit DESC;

17. Top 10 Cities by Sales
SELECT TOP 10
    City,
    SUM(Sales) AS Total_Sales
FROM SalesData_Import
GROUP BY City
ORDER BY Total_Sales DESC;


 18. Top 10 Cities by Profit
SELECT TOP 10
    City,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY City
ORDER BY Total_Profit DESC;


 19. Products/Sub-Categories with Negative Profit
SELECT
    [Sub-Category],
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY [Sub-Category]
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;


 20. Sales and Profit by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Category
ORDER BY Total_Sales DESC;

 21. Sales and Profit by Region
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Region
ORDER BY Total_Sales DESC;

 22. Discount Analysis
SELECT
    Category,
    AVG(Discount) AS Average_Discount,
    SUM(Profit) AS Total_Profit
FROM SalesData_Import
GROUP BY Category
ORDER BY Average_Discount DESC;

 23. Overall Business Summary
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    AVG(Discount) AS Average_Discount
FROM SalesData_Import;