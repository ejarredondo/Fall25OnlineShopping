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

SELECT C.ProductName, SUM(ItemQuantity) AS TotalQuantitySold
FROM ItemSupplied AS ISD
JOIN Transac T On ISD.TransactionID = T.TransactionID
JOIN Catalog C ON ISD.ProductID = C.ProductID
WHERE T.INCOMINGOROUTGOING = 'O'
	AND EXTRACT(Year FROM T.TransactionDate) = 2024 # DEFAULT can't be used in this context so had to change it; pls change if this isn't correct tho
GROUP BY C.ProductName
Order BY TotalQuantitySold DESC
LIMIT 1; 

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




#Average customer spend and item quantity?

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
