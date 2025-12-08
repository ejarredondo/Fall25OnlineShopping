USE OnlineShopping;

INSERT INTO store (StreetAddress, City, State, Zip) 
VALUES ('120 Publix Avenue', 'Seattle', 'WA', '98115');

INSERT INTO store (StreetAddress, City, State, Zip) 
VALUES ('350 Kroger Street', 'Seattle', 'WA', '98115');

INSERT INTO store (StreetAddress, City, State, Zip) 
VALUES ('894 Aldi Circle', 'Seattle', 'WA', '98115');

INSERT INTO customer (first_name, last_name)
VALUES ('Sally', 'Edwards');

INSERT INTO customer (first_name, last_name)
VALUES ('Peter', 'Stuart');

INSERT INTO customer (first_name, last_name)
VALUES ('Marco', 'Anthony');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Jane', 'Doe', '2023-08-15', 35.50, 'Manager', TRUE, '123456789', '98765432101234567', 'jane.doe@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('John', 'Smith', '2024-01-20', 18.00, 'Associate', FALSE, '987654321', '111222333444555', 'john.smith@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Clive', 'Staples', '2024-03-30', 18.50, 'Associate', TRUE, '582084442', '322202939490293', 'clive.staples@company.com');

INSERT INTO department (department_name, employee_total) 
VALUES ('Sales', 60);

INSERT INTO department (department_name, employee_total) 
VALUES ('Stock', 25);

INSERT INTO department (department_name, employee_total) 
VALUES ('Accounting', 30);

INSERT INTO supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, StoreID) 
VALUES ('Global Fresh Produce', '450 Produce Way', 'Seattle', 'WA', '98115', 3);

INSERT INTO supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, StoreID) 
VALUES ('Tri-State Bakery', '230 Dough Street', 'Seattle', 'WA', '98115', 4);

INSERT INTO supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, StoreID) 
VALUES ('Meats & Co', '124 Oinkmoo Road', 'Seattle', 'WA', '98115', 5);

INSERT INTO catalog (product_name, category, sku, base_price, sale_price, sold_by_weight_or_unit, brand, quantity_of_item, department_id, expiration_date)
VALUES ('Organic Coffee', 'Beverages', 4001, 1.00, 15.99, 'Unit', 'Beanery Best', 500, 1, '2027-12-15');

INSERT INTO catalog (product_name, category, sku, weight, base_price, sale_price, sold_by_weight_or_unit, brand, quantity_of_item, department_id, expiration_date)
VALUES ('Premium Steak', 'Meats', 4002, 5.62, 7.00, 5.00, 'Weight', 'Cattle Co.', 20, 2, '2025-12-30');

INSERT INTO catalog (product_name, category, sku, base_price, sale_price, sold_by_weight_or_unit, brand, quantity_of_item, department_id, expiration_date)
VALUES ('Sourdough Bread', 'Bakery', 4003, 5.00, 5.00, 'Unit', 'The French Baker', 30, 3, '2026-01-18');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate) 
VALUES (1, 'I', 26.87, '2023-12-04 15:45:36');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate)
VALUES (2, 'O', 257.50, '2024-05-16 08:36:57');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing,TransactionAmount , TransactionDate) 
VALUES (3, 'I', 21.67, '2025-10-15 10:32:26');

INSERT INTO itemsupplied (product_id, transaction_id, supplier_id, store_id, item_quantity)
VALUES (1, 2, 1, 1, 15);

INSERT INTO itemsupplied (product_id, transaction_id, supplier_id, store_id, item_quantity)
VALUES (2, 3, 2, 2, 20);

INSERT INTO itemsupplied (product_id, transaction_id, supplier_id, store_id, item_quantity)
VALUES (3, 1, 3, 3, 45);

INSERT INTO dietaryinformation (product_id, restriction)
VALUES (1, 'keto');

INSERT INTO dietaryinformation (product_id, restriction)
VALUES (2, 'kosher');

INSERT INTO dietaryinformation (product_id, restriction)
VALUES (3, 'GlutenFree');

INSERT INTO employeetransaction (employee_id, transaction_id, store_id)
VALUES (1, 2, 1);

INSERT INTO employeetransaction (employee_id, transaction_id, store_id)
VALUES (2, 3, 2);

INSERT INTO employeetransaction (employee_id, transaction_id, store_id)
VALUES (3, 1, 3);

INSERT INTO customerpurchasehistory (customer_id, transaction_id, amount_spent, date_purchased, time_purchased)
VALUES (1, 2, 34.50, '2025-05-06', '10:25:46');

INSERT INTO customerpurchasehistory (customer_id, transaction_id, amount_spent, date_purchased, time_purchased)
VALUES (2, 3, 24.57, '2025-10-23', '15:46:12');

INSERT INTO customerpurchasehistory (customer_id, transaction_id, amount_spent, date_purchased, time_purchased)
VALUES (3, 1, 123.56, '2025-08-17', '12:56:28');

INSERT INTO customertransaction (customer_id, transaction_id, shipping_address_street, shipping_address_city, shipping_address_state, shipping_address_zip, card_info, email_address, items_purchased)
VALUES (1, 2, '123 Leaf Avenue', 'Seattle', 'WA', '98115', '1234567890123456', 'joesmith@gmail.com', 15);

INSERT INTO customertransaction (customer_id, transaction_id, shipping_address_street, shipping_address_city, shipping_address_state, shipping_address_zip, card_info, email_address, items_purchased)
VALUES (2, 3, '45 Food Street', 'Seattle', 'WA', '98115', '7894561278945612', 'rebekahjones@hotmail.com', 7);

INSERT INTO customertransaction (customer_id, transaction_id, shipping_address_street, shipping_address_city, shipping_address_state, shipping_address_zip, card_info, email_address, items_purchased)
VALUES (3, 1, '28 Famous Person Way', 'Seattle', 'WA', '98115', '12579057913045672','samanthapearson@outlook.com', 11);
