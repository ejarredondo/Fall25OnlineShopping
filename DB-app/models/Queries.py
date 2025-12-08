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
        C.ProductName, 
        Sum(ISD.ItemQuantity) AS Total_Quantity_Sold,
        FROM ItemSupplied ISD
        JOIN Transaction T ON ISD.TransactionID = T.TransactionID
        JOIN Catalog C ON ISD.ProductID = C.ProductID
        WHERE T.INCOMINGOROUTGOING = 'O'
                 AND Year(T.TransactionDate) = 2024
        GROUP BY C.ProductName
        ORDER BY Total_Quantity_Sold ASC
        LIMIT 1;"""))
    return ProductSoldLeast

def get_avg_Spend_And_Item_Quantity(): 
    avg_spend_and_quantity = db.session.execute(text("""SELECT
        C.CustomerID,C.FirstName, C.LastName,
        SUM(CPH.AmountSpent) AS Total_spent,
        SUM(ISD.ItemQuantity) AS Total_items_purchased,
        AVG(CPH.AmountSpent) AS Avg_Spent_Per_Transaction,
        AVG(ISD.ItemQuantity) AS Avg_Items_Per_Transaction
        FROM Customer C
        JOIN CustomerPurchasehistory CPH ON C.CustomerID = CPH.CustomerID
        JOIN Transaction T ON CPH.TransactionID = T.TransactionID
        JOIN ItemSupplied ISD ON T.TransactionID = ISD.TransactionID
        WHERE T.IncomingOrOutgoing = 'O'
        GROUP BY C.CustomerID, C.FirstName, C.LastName
        ORDER BY AVG_Spent_Per_Transaction DESC;"""))
    return avg_spend_and_quantity

def get_products_by_seasonality(): 
    products_by_season = db.session.execute(text("""SELECT C.ProductName,C.category,
        DI.Restriction AS DietaryRestriction
        CASE
         WHEN Month(CurDate()) IN (12, 1, 2) Then 'Winter'
	    WHEN Month(CurDate()) IN (3, 4, 5) Then 'Spring'
	    WHEN Month(CurDate()) IN (6, 7, 8) Then 'Summer'
	    WHEN Month(CurDate()) IN (9, 10, 11) Then 'Autumn'
	    ELSE 'Unknown'
      End AS CurrentSeason
    FROM Catalog C
    LEFT JOIN DietaryInformation DI ON C.ProductID = DI.ProductID
    ORDER BY C.Category, CurrentSeason, C.ProductName
;"""))
    return products_by_season.all()

def get_avg_items_supplied_per_year(): 
    avg_supplied_items = db.session.execute(text("""SELECT  
    T.TransactionID as TransactionID, 
	S.SupplierID as SupplierID, 
    S.SupplierName as SupplierName, 
    YEAR(T.TransactionDate) as YearOfTransaction,
    AVG(ISD.ItemQuantity) as AvgItemsSupplied
FROM Transaction T
JOIN ItemSupplied ISD ON T.TransactionID = ISD.TransactionID
JOIN Supplier S ON ISD.SupplierID = S.SupplierID
WHERE T.IncomingOrOutgoing = 'I'
GROUP BY TransactionID, SupplierID, SupplierName
ORDER BY YearOfTransaction;"""))
    return avg_supplied_items.all()
