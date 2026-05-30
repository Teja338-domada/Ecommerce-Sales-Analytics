-- Total Sales
SELECT SUM(Sales) AS TotalSales
FROM Orders;

-- Total Profit
SELECT SUM(Profit) AS TotalProfit
FROM Orders;

-- Sales by Region
SELECT Region,
       SUM(Sales) AS TotalSales
FROM Orders
GROUP BY Region
ORDER BY TotalSales DESC;

-- Profit by Category
SELECT Category,
       SUM(Profit) AS TotalProfit
FROM Orders
GROUP BY Category
ORDER BY TotalProfit DESC;

-- Top 10 Selling Sub-Categories
SELECT [Sub-Category],
       SUM(Sales) AS TotalSales
FROM Orders
GROUP BY [Sub-Category]
ORDER BY TotalSales DESC;