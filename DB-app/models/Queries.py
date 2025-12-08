from sqlalchemy import text
from core import ma, db

def get_least_stocked_products():
    least_stocked_products = db.session.execute(text("""SELECT
        C.DepartmentID AS DepartmentID,
        C.ProductID AS ProductID,
        C.ProductName AS ProductName,
        MIN(C.QuantityofItem) AS QuantityofItem
        FROM Catalog C
        GROUP BY C.DepartmentID, C.ProductID, C.ProductName
        ORDER BY C.DepartmentID, C.ProductName;"""))
    return least_stocked_products.all()

def get_products_expiring_soon():
    products_expiring_soon = db.session.execute(text("""SELECT
        C.ProductID AS ProductID,
        C.ProductName AS ProductName,
        C.ExpirationDate AS ExpirationDate
        FROM Catalog C
        WHERE C.ExpirationDate IS NOT NULL
        ORDER BY C.ExpirationDate ASC;"""))
    return products_expiring_soon.all()

def get_product_sold_most(year=2024):
    product_sold_most = db.session.execute(text("""SELECT
        C.ProductName AS ProductName,
        SUM(ISD.ItemQuantity) AS TotalQuantitySold
        FROM ItemSupplied AS ISD
        JOIN Transac T ON ISD.TransactionID = T.TransactionID
        JOIN Catalog C ON ISD.ProductID = C.ProductID
        WHERE T.IncomingOrOutgoing = 'O'
            AND EXTRACT(YEAR FROM T.TransactionDate) = :year
        GROUP BY C.ProductName
        ORDER BY TotalQuantitySold DESC
        LIMIT 1;"""), {'year': year})
    return product_sold_most

def get_Product_Sold_Least(): 
    ProductSoldLeast = db.session.execute(text("""SELECT 
        C.product_name, 
        SUM(ISD.item_quantity) AS total_quantity_sold
        FROM ItemSupplied ISD
        JOIN Transaction T ON ISD.transaction_id = T.transaction_id
        JOIN Catalog C ON ISD.product_id = C.product_id
        WHERE T.incoming_or_outgoing = 'O'
              AND YEAR(T.transaction_date) = 2024
        GROUP BY C.product_name
        ORDER BY total_quantity_sold ASC
        LIMIT 1;"""))
    return ProductSoldLeast

def get_avg_Spend_And_Item_Quantity(): 
    avg_spend_and_quantity = db.session.execute(text("""SELECT
        C.customer_id, C.first_name, C.last_name,
        SUM(CPH.amount_spent) AS total_spent,
        SUM(ISD.item_quantity) AS total_items_purchased,
        AVG(CPH.amount_spent) AS avg_spent_per_transaction,
        AVG(ISD.item_quantity) AS avg_items_per_transaction
        FROM Customer C
        JOIN CustomerPurchasehistory CPH ON C.customer_id = CPH.customer_id
        JOIN Transaction T ON CPH.transaction_id = T.transaction_id
        JOIN ItemSupplied ISD ON T.transaction_id = ISD.transaction_id
        WHERE T.incoming_or_outgoing = 'O'
        GROUP BY C.customer_id, C.first_name, C.last_name
        ORDER BY avg_spent_per_transaction DESC;"""))
    return avg_spend_and_quantity

def get_products_by_seasonality(): 
    products_by_season = db.session.execute(text("""SELECT C.product_name,C.category,
        DI.restriction AS dietary_restriction
        CASE
         WHEN Month(CurDate()) IN (12, 1, 2) Then 'Winter'
	    WHEN Month(CurDate()) IN (3, 4, 5) Then 'Spring'
	    WHEN Month(CurDate()) IN (6, 7, 8) Then 'Summer'
	    WHEN Month(CurDate()) IN (9, 10, 11) Then 'Autumn'
	    ELSE 'Unknown'
      End AS CurrentSeason
    FROM Catalog C
    LEFT JOIN DietaryInformation DI ON C.product_id = DI.product_id
    ORDER BY C.category, CurrentSeason, C.product_name
;"""))
    return products_by_season.all()

def get_avg_items_supplied_per_year(): 
    avg_supplied_items = db.session.execute(text("""SELECT  
    T.transaction_id as transaction_id, 
	S.supplier_id as supplier_id, 
    S.supplier_name as supplier_name, 
    YEAR(T.transaction_date) as year_of_transaction,
    AVG(ISD.item_quantity) as avg_items_supplied
FROM Transaction T
JOIN ItemSupplied ISD ON T.transaction_id = ISD.transaction_id
JOIN Supplier S ON ISD.supplier_id = S.supplier_id
WHERE T.incoming_or_outgoing = 'I'
GROUP BY TransactionID, supplier_id, supplier_name
ORDER BY year_of_transaction;"""))
    return avg_supplied_items.all()
