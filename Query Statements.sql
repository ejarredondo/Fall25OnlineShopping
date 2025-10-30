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


#Average customer spend and item quantity?

