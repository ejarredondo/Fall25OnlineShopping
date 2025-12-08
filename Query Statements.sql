1.What products do we have the least of (per department and overall)?

SELECT C.department_id AS DepartmentID,
        C.product_id AS ProductID,
        C.product_name AS ProductName,
        MIN(C.quantity_of_item) AS QuantityofItem
        FROM catalog C
        GROUP BY C.department_id, C.product_id, C.product_name
        ORDER BY C.department_id, C.product_name;

2.What products are expiring soonest?

SELECT C.product_id AS ProductID,
        C.product_name AS ProductName,
        C.expirataion_date AS ExpirationDate
        FROM catalog C
        WHERE C.expiration_date IS NOT NULL
        ORDER BY C.expiration_date ASC;

3.What product was sold the most during a given year? 

SELECT C.product_name AS ProductName,
        SUM(ISD.item_quantity) AS TotalQuantitySold
        FROM item_supplied AS ISD
        JOIN transaction T ON ISD.transaction_id = T.transaction_id
        JOIN catalog C ON ISD.product_id = C.product_id
        WHERE T.incoming_or_outgoing = 'O'
            AND EXTRACT(YEAR FROM T.transaction_date) = :year
        GROUP BY C.product_name
        ORDER BY totalQ_quantity_sold DESC
        LIMIT 1;

4.What product was sold the least during a given year? 

SELECT C.product_name,
	SUM( ISD.item_quantity) AS total_quantity_sold
FROM ItemSupplied ISD
JOIN Transaction T On ISD.transaction_id = T.transaction_id
JOIN Catalog C ON ISD.product_id = C.product_id
WHERE T.incoming_or_outgoing = 'O'
	AND EXTRACT(Year FROM T.transaction_date) = 2024 # see above comment
GROUP BY C.product_name
Order BY total_quantity_sold ASC
LIMIT 1;


5.Average customer spend and item quantity?

SELECT C.customer_id, C.first_name, C.last_name, 
SUM(CPH.amount_spent) AS total_spent,
SUM(ISD.ItemQuantity) AS total_items_purchased, 
AVG(CPH.AmountSpent) AS avg_spent_per_transaction,
AVG(ISD.ItemQuantity) AS avg_items_per_transaction
FROM Customer C
JOIN customer_purchase_history CPH ON C.customer_id = CPH.customer_id
JOIN Transaction T ON CPH.transaction_id = T.transaction_id
JOIN ItemSupplied ISD ON T.transaction_id = ISD.transaction_id
WHERE T.incoming_or_outgoing = 'O'
GROUP BY C.customer_id, C.first_name, C.last_name
ORDER BY avg_spent_per_transaction DESC;

6.Products by Category,Restrictions, or Seasonality

SELECT C.product_name, C.category, DI.restriction AS dietary_restriction,
CASE
	WHEN Month(CurDate()) IN (12, 1, 2) Then 'Winter'
	WHEN Month(CurDate()) IN (3, 4, 5) Then 'Spring'
	WHEN Month(CurDate()) IN (6, 7, 8) Then 'Summer'
	WHEN Month(CurDate()) IN (9, 10, 11) Then 'Autumn'
	ELSE 'Unkown'
  End AS CurrentSeason
FROM Catalog C
LEFT JOIN DietaryInformation DI ON C.product_id = DI.product_id
ORDER BY C.category, CurrentSeason, C.product_name;

# average amount of items being supplied in each shipment per year

SELECT T.transaction_id as transaction_id, 
	S.supplier_id as supplier_id, 
    S.supplier_name as supplier_name, 
    YEAR(T.transaction_date) as year_of_transaction,
    AVG(ISD.item_quantity) as avg_items_supplied
FROM Transaction T
JOIN ItemSupplied ISD ON T.transaction_id = ISD.transaction_id
JOIN Supplier S ON ISD.supplier_id = S.supplier_id
WHERE T.incoming_or_outgoing = 'I'
GROUP BY transaction_id, supplier_id, supplier_name
ORDER BY year_of_transaction;

SELECT * FROM transaction;
