from sqlalchemy import text
from core import ma, db

def get_least_stocked_products():
    least_stocked_products = db.session.execute(text("""SELECT
        C.department_id AS DepartmentID,
        C.product_id AS ProductID,
        C.product_name AS ProductName,
        MIN(C.quantity_of_item) AS QuantityofItem
        FROM catalog C
        GROUP BY C.department_id, C.product_id, C.product_name
        ORDER BY C.department_id, C.product_name;"""))
    return least_stocked_products.all()

def get_products_expiring_soon():
    products_expiring_soon = db.session.execute(text("""SELECT
        C.product_id AS ProductID,
        C.product_name AS ProductName,
        C.expiration_date AS ExpirationDate
        FROM catalog C
        WHERE C.expiration_date IS NOT NULL
        ORDER BY C.expiration_date ASC;"""))
    return products_expiring_soon.all()

def get_product_sold_most(year=2024):
    product_sold_most = db.session.execute(text("""SELECT
        C.product_name AS ProductName,
        SUM(ISD.item_quantity) AS TotalQuantitySold
        FROM item_supplied AS ISD
        JOIN transaction T ON ISD.transaction_id = T.transaction_id
        JOIN catalog C ON ISD.product_id = C.product_id
        WHERE T.incoming_or_outgoing = 'O'
            AND EXTRACT(YEAR FROM T.transaction_date) = :year
        GROUP BY C.product_name
        ORDER BY TotalQuantitySold DESC
        ;"""), {'year': year})
    return product_sold_most

def get_Product_Sold_Least(): 
    ProductSoldLeast = db.session.execute(text("""SELECT 
        C.product_name, 
        SUM(ISD.item_quantity) AS total_quantity_sold
        FROM ite_supplied ISD
        JOIN transaction T ON ISD.transaction_id = T.transaction_id
        JOIN catalog C ON ISD.product_id = C.product_id
        WHERE T.incoming_or_outgoing = 'O'
              AND YEAR(T.transaction_date) = 2024
        GROUP BY C.product_name
        ORDER BY total_quantity_sold ASC
        ;"""))
    return ProductSoldLeast

def get_avg_Spend_And_Item_Quantity(): 
    avg_spend_and_quantity = db.session.execute(text("""SELECT
        C.customer_id, C.first_name, C.last_name,
        SUM(CPH.amount_spent) AS total_spent,
        SUM(ISD.item_quantity) AS total_items_purchased,
        AVG(CPH.amount_spent) AS avg_spent_per_transaction,
        AVG(ISD.item_quantity) AS avg_items_per_transaction
        FROM customer C
        JOIN customer_purchase_history CPH ON C.customer_id = CPH.customer_id
        JOIN transaction T ON CPH.transaction_id = T.transaction_id
        JOIN item_supplied ISD ON T.transaction_id = ISD.transaction_id
        WHERE T.incoming_or_outgoing = 'O'
        GROUP BY C.customer_id, C.first_name, C.last_name
        ORDER BY avg_spent_per_transaction DESC;"""))
    return avg_spend_and_quantity

def get_products_by_seasonality(): 
    products_by_season = db.session.execute(text("""SELECT C.product_name,C.category,
        DI.restriction AS dietary_restriction,
        CASE
         WHEN Month(CurDate()) IN (12, 1, 2) Then 'Winter'
	    WHEN Month(CurDate()) IN (3, 4, 5) Then 'Spring'
	    WHEN Month(CurDate()) IN (6, 7, 8) Then 'Summer'
	    WHEN Month(CurDate()) IN (9, 10, 11) Then 'Autumn'
	    ELSE 'Unknown'
      End AS CurrentSeason
    FROM catalog C
    LEFT JOIN dietary_information DI ON C.product_id = DI.product_id
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
FROM transaction T
JOIN item_supplied ISD ON T.transaction_id = ISD.transaction_id
JOIN supplier S ON ISD.supplier_id = S.supplier_id
WHERE T.incoming_or_outgoing = 'I'
GROUP BY transaction_id, supplier_id, supplier_name
ORDER BY year_of_transaction;"""))
    return avg_supplied_items.all()
