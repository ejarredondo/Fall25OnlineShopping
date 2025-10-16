CREATE TABLE Supplier(
	SupplierName 		VARCHAR(255) Unique NOT NULL,
	SupplierID 		INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	SupplierAddressCity	VARCHAR(20),
	SupplierAddressState	VARCHAR(2),
	SupplierAddressZip	VARCHAR(5),
	ItemsSupplied 		XML,
	NumItems 		INT,
	STOREID 		INT,
    	FOREIGN KEY (STOREID) REFERENCES Store (StoreID) 
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);



CREATE TABLE Catalog(
	ProductID 		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	ProductName		VARCHAR(255) NOT NULL,
	Category 		VARCHAR(255)NOT NULL,	
	SKU 			INT NOT NULL UNIQUE,
	Weight 			DECIMAL(5,2),
	BasePrice 		DECIMAL(7,2) NOT NULL CHECK (BasePrice >= 0),
	SalePrice 		DECIMAL(7,2) NOT NULL CHECK (SalePrice >= 0),
	DietaryInformation 	XML,
	SoldByWeightorUnit 	ENUM('Weight', 'Unit') NOT NULL,
	Brand 			VARCHAR(255),
	QuantityofItem 		SMALLINT
);



CREATE TABLE Store (
	StoreID 		INT PRIMARY KEY AUTO_INCREMENT,
	StreetAddress 		VARCHAR(30) NOT NULL,
    	City 			VARCHAR(30) NOT NULL,
    	State 			VARCHAR(2) NOT NULL,
    	Zip 			VARCHAR(5) NOT NULL,
	Inventory 		XML,
	EmployeeNumber		INT NOT NULL,
	FOREIGN KEY (EmployeeNumber) REFERENCES Department(EmployeeTotal)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);

CREATE TABLE Department (
	DepartmentID		INT PRIMARY KEY AUTO_INCREMENT,
	DepartmentName		VARCHAR(20) NOT NULL,
	EmployeeTotal		INT NOT NULL
);


CREATE TABLE Employee (
    	EmployeeID 		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FirstName 		VARCHAR(100) NOT NULL,
	LastName		VARCHAR(100) NOT NULL,
	StartDate 		DATE,
	PayRate 		DECIMAL(8, 2) CHECK (PayRate >=0) NOT NULL,
	Position 		VARCHAR(50),
	Availability 		BOOLEAN,
	BankRoutingInformation 	VARCHAR(9) NOT NULL,
	CheckingAccountNumber 	VARCHAR(17) NOT NULL,
	EmailAddress 		VARCHAR(250)
);

CREATE TABLE Customer (
	CustomerID		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FirstName		VARCHAR(30),
	LastName		VARCHAR(30), 
	Preferences		XML
);

CREATE TABLE CustomerTransaction (
	CustomerID		INT NOT NULL PRIMARY KEY AUTO INCREMENT,
	TransactionID		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	ShippingAddressStreet	VARCHAR(30),
	ShippingAddressCity	VARCHAR(30),
	ShippingAddressState	VARCHAR(2),
	ShippingAddressZip	VARCHAR(5),
	CardInfo		VARCHAR(30) UNIQUE,
	EmailAddress		VARCHAR(30) UNIQUE,
	TransactionAmount	DECIMAL(5,2) NOT NULL,
	ItemsPurchased		SMALL INT,
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
	FOREIGN KEY (TransactionAmount) REFERENCES Transaction(TrasactionAmount)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);
	
CREATE TABLE Transaction (
	TransactionID		SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	CashierEmployeeID	INT NOT NULL PRIMARY KEY,
	IncomingOrOutgoing	ENUM('I', 'O') PRIMARY KEY,
	TransactionAmount	DECIMAL(5,2) NOT NULL CHECK (TransactionAmount >= 0),
	FOREIGN KEY (CashierEmployeeID) REFERENCES Employee(EmployeeID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);

CREATE TABLE EmployeeTransaction (
	EmployeeID		SMALL INT REQUIRED,
	TransactionID		SMALL INT REQUIRED,
	StoreID			SMALL INT REQUIRED,
	FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (TransactionID) REFERENCES Transaction(TransactionID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (StoreID) REFERENCES Store(StoreID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);
