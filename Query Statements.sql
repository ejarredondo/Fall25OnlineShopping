#What products do we have the least of (per department and overall)?

SELECT DepartmentID, ProductID, ProductName, MIN(QuantityofItem)
FROM Catalog
GROUP BY DepartmentID, ProductID, ProductName;

#What products are expiring soonest?

SELECT ProductID, ProductName, ExpirationDate
FROM Catalog
WHERE ExpirationDate IS NOT NULL
ORDER BY ExpirationDate ASC;

#What product was sold the most/least during a given month?

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




#Average customer spend and item quantity?

