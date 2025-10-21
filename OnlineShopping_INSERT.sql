INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID) 
VALUES ('Global Fresh Produce', 50, '450 Produce Way, Seattle, WA', 100);

INSERT INTO Supplier (SupplierName, NumItems, StoreAddress, StoreID)
Values ('Tri-State Bakery', 35, '230 Dough Street, Seattle, WA', 100);

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

INSERT INTO Store (Address) 
VALUES ('120 Publix Avenue, Seattle, WA');

INSERT INTO Store (Address) 
VALUES ('350 Kroger Street, Seattle, WA');

INSERT INTO Store (Address) 
VALUES ('894 Aldi Circle, Seattle, WA');

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Sales', 60);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Stock', 25);

INSERT INTO Department (DepartmentName, EmployeeTotal) 
VALUES ('Accounting', 30);

INSERT INTO Transaction (Cashier, IncomingOrOutgoing, TransactionAmount) 
VALUES ('Jeremy', 'I', 26.87);

INSERT INTO Transaction (Cashier, IncomingOrOutgoing, TransactionAmount) 
VALUES ('Sarah', 'O', 257.50);

INSERT INTO Transaction (Cashier, IncomingOrOutgoing, TransactionAmount) 
VALUES ('Lily', 'I', 21.67);