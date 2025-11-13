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

SELECT C.ProductName, SUM(ItemQuantity) AS TotalQuantitySold
FROM ItemSupplied AS ISD
JOIN Transac T On ISD.TransactionID = T.TransactionID
JOIN Catalog C ON ISD.ProductID = C.ProductID
WHERE T.INCOMINGOROUTGOING = 'O'
	AND EXTRACT(Year FROM T.TransactionDate) = 2024 # DEFAULT can't be used in this context so had to change it; pls change if this isn't correct tho
GROUP BY C.ProductName
Order BY TotalQuantitySold DESC
LIMIT 1; 

4.What product was sold the least during a given year? 

SELECT C.ProductName,
	SUM( ISD.ItemQuantity) AS TotalQuantitySold
FROM ItemSupplied ISD
JOIN Transac T On ISD.TransactionID = T.TransactionID
JOIN Catalog C ON ISD.ProductID = C.ProductID
WHERE T.INCOMINGOROUTGOING = 'O'
	AND EXTRACT(Year FROM T.TransactionDate) = 2024 # see above comment
GROUP BY C.ProductName
Order BY TotalQuantitySold ASC
LIMIT 1;


5.Average customer spend and item quantity?

SELECT C.CustomerID, C.FirstName, C.LastName, 
SUM(CPH.AmountSpent) AS Totalspent,
SUM(ISD.ItemQuantity) AS TotalItemsPurchased, 
AVG(CPH.AmountSpent) AS AvgSpentPerTransaction,
AVG(ISD.ItemQuantity) AS AvgItemsPerTransaction
FROM Customer C
JOIN CustomerPurchaseHistory CPH ON C.CustomerID = CPH.CustomerID
JOIN Transac T ON CPH.TransactionID = T.TransactionID
JOIN ItemSupplied ISD ON T.TransactionID = ISD.TransactionID
WHERE T.IncomingOrOutgoing = 'O'
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY AvgSpentPerTransaction DESC;

<<<<<<< HEAD
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
=======
# average amount of items being supplied in each shipment per year

SELECT T.TransactionID as TransactionID, 
	S.SupplierID as SupplierID, 
    S.SupplierName as SupplierName, 
    YEAR(T.TransactionDate) as YearOfTransaction,
    AVG(ISD.ItemQuantity) as AvgItemsSupplied
FROM Transac T
JOIN ItemSupplied ISD ON T.TransactionID = ISD.TransactionID
JOIN Supplier S ON ISD.SupplierID = S.SupplierID
WHERE T.IncomingOrOutgoing = 'I'
GROUP BY TransactionID, SupplierID, SupplierName
ORDER BY YearOfTransaction;
>>>>>>> 3b6abcd2149b75db34f39078fd8c41bcfbda64f9
