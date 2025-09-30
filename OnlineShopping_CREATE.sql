CREATE TABLE Supplier(
SupplierName VARCHAR(255) Unique NOT NULL,
SupplierID INT PRIMARY KEY,
ItemsSupplied XML,
NumeItems INT,
StoreAdress VARCHAR(255) Unique NOT NUll,
STOREID INT
);

create table Catalog(
ProductID int NOT NULL,
ProductName varchar(255) NOT NULL,
Category varchar(255)NOT NULL,
SKU int NOT NULL,
Weight decimal(5,2),
BasePrice decimal(5,2) NOT NULL,
SalePrice decimal(5,2),
DietaryInformation XML,
SoldByWeightorUnit varchar(7) NOT NULL,
Brand varchar(255),
QuantityofItem smallint
);


CREATE TABLE Store (
	StoreID INT,
	Address VARCHAR(30) NOT NULL,
	Inventory XML,
	DepartmentID INT NOT NULL,
	Department VARCHAR(20) NOT NULL,
	Employee INT NOT NULL,
	PRIMARY KEY (StoreID)
);
