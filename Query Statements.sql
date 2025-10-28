#What products do we have the least of (per department and overall)?

SELECT ProductName, ProductId, min(QuantityofItem)
FROM Catalog
GROUP BY DepartmentID;

#What products are expiring soonest?
SELECT 
 	ProductID,
	ProductName,
	ExpirationDate,
FROM 
	Catalog
WHERE
	ExpirationDate IS NOT NULL
ORDER BY
	ExpirationDate ASC;


#What product was sold the most/least during a given month?


#Average customer spend and item quantity?

