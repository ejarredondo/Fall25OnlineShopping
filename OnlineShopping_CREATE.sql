CREATE TABLE Supplier(
SupplierName VARCHAR(255) Unique NOT NULL,
SupplierID INT PRIMARY KEY,
ItemsSupplied XML,
NumeItems INT,
StoreAdress VARCHAR(255) Unique NOT NUll,
STOREID INT
);