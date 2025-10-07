CREATE TABLE Supplier(
	SupplierName VARCHAR(255) Unique NOT NULL,
	SupplierID INT PRIMARY KEY,
	ItemsSupplied XML,
	NumeItems INT,
	StoreAdress VARCHAR(255) Unique NOT NUll,
	STOREID INT
);


CREATE TABLE Catalog(
	ProductID INT NOT NULL PRIMARY KEY,
	ProductName VARCHAR(255) NOT NULL,
	Category VARCHAR(255)NOT NULL,	
	SKU int NOT NULL,
	Weight DECIMAL(5,2),
	BasePrice DECIMAL(5,2) NOT NULL,
	SalePrice DECIMAL(5,2),
	DietaryInformation XML,
	SoldByWeightorUnit VARCHAR(7) NOT NULL,
	Brand VARCHAR(255),
	QuantityofItem SMALLINT
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


CREATE TABLE Employee (
	Name VARCHAR(100),
	StartDate DATE,
	PayRate DECIMAL(8, 2),
	Position VARCHAR(50),
	Availability BOOLEAN,
	BankRoutingInformation VARCHAR(9),
	CheckingAccountNumber VARCHAR(17),
	EmailAddress VARCHAR(250),
);

CREATE TABLE Customer (
	Name	VARCHAR(30), 
	Preferences	XML
);

CREATE TABLE CustomerTransaction (
	CustomerID	INT NOT NULL PRIMARY KEY,
	TransactionID	INT NOT NULL PRIMARY KEY,
	ShippingAddress	VARCHAR(30),
	CardInfo	VARCHAR(30) UNIQUE,
	EmailAddress	VARCHAR(30) UNIQUE,
	TransactionAmount	DECIMAL(5,2),
	ItemsPurchased	SMALL INT
);
	
CREATE TABLE Transaction (
	Cashier			VARCHAR(30) PRIMARY KEY,
	IncomingOrOutgoing	VARCHAR(1) PRIMARY KEY
);

CREATE TABLE EmployeeTransaction (
	EmployeeID	SMALL INT PRIMARY KEY,
	TransactionID	SMALL INT PRIMARY KEY,
	StoreID		SMALL INT REQUIRED
);
