INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID) 
VALUES ('Global Fresh Produce', 50, '450 Produce Way, Seattle, WA', 100);

INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID)
Values ('Tri-State Bakery' 35, '230 Dough Street, Seattle, WA', 100);

INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID)
Values ('Meats & Co', 100, '124 Oinkmoo Road, Seattle, WA', 100);


INSERT INTO Catalog (ProductName, Category, SKU, Weight, BasePrice, SoldByWeightOrUnit, Brand, QuantityofItem)
VALUES ('Organic Coffee', 'Beverages', 4001, 1.00, 15.99, 'Unit', 'Beanery Best', 500);

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SalePrice, SoldByWeightOrUnit, Brand, QuantityofItem)
VALUES ('Premium Steak', 'Meats', 4002, 7.00, 5.00, 'Weight', 'Cattle Co.', 20);

INSERT INTO Catalog (ProductName, Category, SKU, BasePrice, SoldByWeightOrUnit, QuantityofItem)
VALUES ('Sourdough Bread', 'Bakery', 4003, 5.00, 'Unit', 30);

INSERT INTO Employee (Name, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Jane Doe', '2023-08-15', 35.50, 'Manager', TRUE, '123456789', '98765432101234567', 'jane.doe@company.com');

INSERT INTO Employee (Name, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('John Smith', '2024-01-20', 18.00, 'Associate', FALSE, '987654321', '111222333444555', 'john.smith@company.com');

INSERT INTO Employee (Name, StartDate, PayRate, Position, Availability, BankRoutingInformation, CheckingAccountNumber, EmailAddress)
VALUES ('Clive Staples', '2024-03-30', 18.50, 'Associate', TRUE, '582084442', '322202939490293', 'clive.staples@company.com');
