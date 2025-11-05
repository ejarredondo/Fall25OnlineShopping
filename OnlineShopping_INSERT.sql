USE OnlineShopping;

INSERT INTO Store (StreetAddress, City, State, Zip) 
VALUES ('120 Publix Avenue', 'Seattle', 'WA', '98115');

INSERT INTO Store (StreetAddress, City, State, Zip) 
VALUES ('350 Kroger Street', 'Seattle', 'WA', '98115');

INSERT INTO Store (StreetAddress, City, State, Zip) 
VALUES ('894 Aldi Circle', 'Seattle', 'WA', '98115');

INSERT INTO Customer(FirstName, LastName)
VALUES ('Sally', 'Edwards');

INSERT INTO Customer (FirstName, LastName)
VALUES ('Peter', 'Stuart');

INSERT INTO Customer (FirstName, LastName)
VALUES ('Marco', 'Anthony');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Jane', 'Doe', '2023-08-15', 35.50, 'Manager', TRUE, '123456789', '98765432101234567', 'jane.doe@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('John', 'Smith', '2024-01-20', 18.00, 'Associate', FALSE, '987654321', '111222333444555', 'john.smith@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Clive', 'Staples', '2024-03-30', 18.50, 'Associate', TRUE, '582084442', '322202939490293', 'clive.staples@company.com');

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Sales', 60);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Stock', 25);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Accounting', 30);

INSERT INTO Supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, STOREID) 
VALUES ('Global Fresh Produce', '450 Produce Way', 'Seattle', 'WA', '98115', 1);

INSERT INTO Supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, STOREID) 
Values ('Tri-State Bakery', '230 Dough Street', 'Seattle', 'WA', '98115', 2);

INSERT INTO Supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, STOREID) 
Values ('Meats & Co', '124 Oinkmoo Road', 'Seattle', 'WA', '98115', 3);

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem, DepartmentID, ExpirationDate)
VALUES ('Organic Coffee', 'Beverages', 4001, 1.00, 15.99, 'Unit', 'Beanery Best', 500, 1, '2027-12-15');

INSERT INTO Catalog (ProductName, Category, SKU, Weight, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem, DepartmentID, ExpirationDate)
VALUES ('Premium Steak', 'Meats', 4002, 5.62, 7.00, 5.00, 'Weight', 'Cattle Co.', 20, 2, '2025-12-30');

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem, DepartmentID, ExpirationDate)
VALUES ('Sourdough Bread', 'Bakery', 4003, 5.00, 5.00, 'Unit', 'The French Baker', 30, 3, '2026-01-18');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate) 
VALUES (1, 'I', 26.87, '2023-12-04 15:45:36');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate)
VALUES (2, 'O', 257.50, '2024-05-16 08:36:57');

INSERT INTO Transac (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate) 
VALUES (3, 'I', 21.67, '2025-10-15 10:32:26');

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ItemQuantity)
Values (1, 2, 1, 1, 15);

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ItemQuantity)
Values (2, 3, 2, 2, 20);

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ItemQuantity)
Values (3, 1, 3, 3, 45);

INSERT INTO DietaryInformation (ProductID, Restriction)
Values (1, 'Keto');

INSERT INTO DietaryInformation (ProductID, Restriction)
Values (2, 'Kosher');

INSERT INTO DietaryInformation (ProductID, Restriction)
Values (3, 'GlutenFree');

INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (1, 2, 1);

INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (2, 3, 2);

INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (3, 1, 3);

INSERT INTO CustomerPurchaseHistory (CustomerID, TransactionID, Amountspent, DatePurchased, TimePurchased)
VALUES (1, 2, 34.50, '2025-05-06', '10:25:46');

INSERT INTO CustomerPurchaseHistory (CustomerID, TransactionID, Amountspent, DatePurchased, TimePurchased)
VALUES (2, 3, 24.57, '2025-10-23', '15:46:12');

INSERT INTO CustomerPurchaseHistory (CustomerID, TransactionID, Amountspent, DatePurchased, TimePurchased)
VALUES (3, 1, 123.56, '2025-08-17', '12:56:28');

INSERT INTO CustomerTransaction (CustomerID, TransactionID, ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, ItemsPurchased)
VALUES (1, 2, '123 Leaf Avenue', 'Seattle', 'WA', '98115', '1234567890123456', 'joesmith@gmail.com', 15);

INSERT INTO CustomerTransaction (CustomerID, TransactionID, ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, ItemsPurchased)
VALUES (2, 3, '45 Food Street', 'Seattle', 'WA', '98115', '7894561278945612', 'rebekahjones@hotmail.com', 7);

INSERT INTO CustomerTransaction (CustomerID, TransactionID, ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, ItemsPurchased)
VALUES (3, 1, '28 Famous Person Way', 'Seattle', 'WA', '98115', '12579057913045672','samanthapearson@outlook.com', 11);
