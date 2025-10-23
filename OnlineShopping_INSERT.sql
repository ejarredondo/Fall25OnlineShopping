INSERT INTO Supplier (SupplierName, SupplierAddressStreet, SupplierAddressCity, SupplierAddressState, SupplierAddressZip, StoreID) 
VALUES ('Global Fresh Produce', '450 Produce Way’, ‘Seattle’, ‘WA', ‘98115’, 100);

INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID)
Values ('Tri-State Bakery', '230 Dough Street’, ‘Seattle’, ‘WA', ‘98115’, 100);

INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID)
Values ('Meats & Co', '124 Oinkmoo Road’, ‘Seattle’, ‘WA', ‘98115’, 100);

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ProductName, ItemQuantity)
Values (12, 15, 6, 100, ‘Honeycrisp Apple’, 15)

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ProductName, ItemQuantity)
Values (25, 85, 45, 100, ‘Ramen Noodles’, 20)

INSERT INTO ItemSupplied (ProductID, TransactionID, SupplierID, StoreID, ProductName, ItemQuantity)
Values (56, 87, 61, 100, ‘Wheat Bread’, 45)

INSERT INTO Catalog (ProductName, Category, SKU, Weight, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem)
VALUES ('Organic Coffee', 'Beverages', 4001, 1.00, 15.99, 'Unit', 'Beanery Best', 500);

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem)
VALUES ('Premium Steak', 'Meats', 4002, 7.00, 5.00, 'Weight', 'Cattle Co.', 20);

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SoldByWeightOrUnit, QuantityofItem)
VALUES ('Sourdough Bread', 'Bakery', 4003, 5.00, 'Unit', 30);

INSERT INTO DietaryInformation (ProductID, ProductName, Restriction)
Values (86, ‘Corn Tortilla’, ‘GlutenFree’)

INSERT INTO DietaryInformation (ProductID, ProductName, Restriction)
Values (79, ‘Soy Milk’, ‘DairyFree’)

INSERT INTO DietaryInformation (ProductID, ProductName, Restriction)
Values (46, ‘Coke Zero’, ‘SugarFree’)

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Jane’, ‘Doe', '2023-08-15', 35.50, 'Manager', TRUE, '123456789', '98765432101234567', 'jane.doe@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('John’, ‘Smith', '2024-01-20', 18.00, 'Associate', FALSE, '987654321', '111222333444555', 'john.smith@company.com');

INSERT INTO Employee (FirstName, LastName, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Clive’, ‘Staples', '2024-03-30', 18.50, 'Associate', TRUE, '582084442', '322202939490293', 'clive.staples@company.com');

INSERT INTO Store (StreetAddress, City, State, Zip, EmployeeNumber) 
VALUES ('120 Publix Avenue’, ‘Seattle’, ‘WA', ‘98115’, 152);

INSERT INTO Store (StreetAddress, City, State, Zip, EmployeeNumber) 
VALUES ('350 Kroger Street’, ‘Seattle’, ‘WA', ‘98115’, 78);

INSERT INTO Store (StreetAddress, City, State, Zip, EmployeeNumber) 
VALUES ('894 Aldi Circle’, ‘Seattle’, ‘WA', ‘98115’, 89);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Sales', 60);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Stock', 25);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Accounting', 30);

INSERT INTO Transaction (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate) 
VALUES (5, 'I', 26.87, 2023-12-04 15:45:36);

INSERT INTO Transaction (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate)
VALUES (10, 'O', 257.50, 2024-05-16 08:36:57);

INSERT INTO Transaction (CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate) 
VALUES (15, 'I', 21.67, 2025-10-15 10:32:26);
INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (45, 85, 100)

INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (86, 123, 100)

INSERT INTO EmployeeTransaction (EmployeeID, TransactionID, StoreID)
VALUES (456, 89, 100)

INSERT INTO CustomerTransaction (ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, TransactionAmount, ItemsPurchased)
VALUES (‘123 Leaf Avenue’, ‘Seattle’, ‘WA’, ‘98115’, ‘1234567890123456’, ‘joesmith@gmail.com’, 123.05, 15)

INSERT INTO CustomerTransaction (ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, TransactionAmount, ItemsPurchased)
VALUES (‘45 Food Street’, ‘Seattle’, ‘WA’, ‘98115’, ‘7894561278945612’, ‘rebekahjones@hotmail.com, 56.39, 7)

INSERT INTO CustomerTransaction (ShippingAddressStreet, ShippingAddressCity, ShippingAddressState, ShippingAddressZip, CardInfo, EmailAddress, TransactionAmount, ItemsPurchased)
VALUES (‘28 Famous Person Way’, ‘Seattle’, ‘WA’, ‘98115’, ‘samanthapearson@outlook.com’, 89.15, 11)
