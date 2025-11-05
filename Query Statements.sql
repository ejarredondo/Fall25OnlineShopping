1.What products do we have the least of (per department and overall)?

SELECT DepartmentID, ProductID, ProductName, MIN(QuantityofItem)
FROM Catalog
GROUP BY DepartmentID, ProductID, ProductName;

2.What products are expiring soonest?

SELECT ProductID, ProductName, ExpirationDate
FROM Catalog
WHERE ExpirationDate IS NOT NULL
ORDER BY ExpirationDate ASC;

3.What product was sold the most during a given year? 

SELECT C.ProductName,
	SUM( IS.ItemQuantity) AS TotalQuantotySold
FROM ItemSupplied IS
JOIN Transaction T On IS.TransactionID = T.TransactionID
JOIN Catalog C ON IS.ProductID = C.ProductID
WHERE T.INCOMINGOROUTGOING = 'O'
	AND EXTRACT(Year FROM T.TransactionDate) = Default
Group BY C.ProductName
Order BY TotalQuantitySold DESC
LIMIT 1; 

4.What product was sold the least during a given year? 

SELECT C.ProductName,
	SUM( IS.ItemQuantity) AS TotalQuantotySold
FROM ItemSupplied IS
JOIN Transaction T On IS.TransactionID = T.TransactionID
JOIN Catalog C ON IS.ProductID = C.ProductID
WHERE T.INCOMINGOROUTGOING = 'O'
	AND EXTRACT(Year FROM T.TransactionDate) = Default
Group BY C.ProductName
Order BY TotalQuantitySold ASC
LIMIT 1;


5.Average customer spend and item quantity?

SELECT C.CustomerID, C.FirstName, C.LastName, 
SUM (CPH.AmountSpent) AS Totalspent,
Sum (IS.ItemQuantity) AS TotalItemsPurchased, 
Avg(CPH.AmountSpent) AS AvgSpendtPerTransaction,
Avg(IS.ItemQuantity) AS AvgItemsPerTransaction
FROM Customer C
JOIN CustomerPurchaseHistory CPH ON C.CustomerID = CPH.CustomerID
JOIN Transaction T ON CPH.TransactionID = T.TransactionID
JOIN ItemsSupplied IS ON T.TransactionID = IS.TransactionID
WhHERE T.IncomingOrOutgoing = 'O'
GROPU BY C.CustomerID, C.FirstName, C.LastName
ORDER BY AvgSpentPerTransaction DESC;

6.Products by Category,Restrictions, or Seasonality

SELECT C.Productname, C.Category, DI.Restriction AS DietaryRestriction
CASE
	WHEN Month(CurDate()) IN (12, 1, 2) Then 'Winter'
	WHEN Month(CurDate()) IN (3, 4, 5) Then 'Spring'
	WHEN Month(CurDate()) IN (6, 7, 8) Then 'Summer'
	WHEN Month(CurDate()) IN (9, 10, 11) Then 'Autumn'
	ELSE 'Unkown'
  End AS CurrentSeason
FROM Catalog C
LEFT JOIN DietaryInformation DI ON C.ProductID = DI.ProductID
ORDER BY C.Category, CurrentSeason, C.ProductName;
