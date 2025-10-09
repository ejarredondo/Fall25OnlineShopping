DROP SCHEMA IF EXISTS OnlineShopping;
CREATE DATABASE OnlineShopping;
USE OnlineShopping;

CREATE TABLE Supplier(
	SupplierID 		INT PRIMARY KEY AUTO_INCREMENT NOT NULL,	
	SupplierName 		VARCHAR(255) UNIQUE NOT NULL,
	ItemsSupplied 		XML,
	NumItems 		INT,
	StoreAddress 		VARCHAR(255) UNIQUE NOT NULL,
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
	Address 		VARCHAR(30) NOT NULL,
	Inventory 		XML,
	DepartmentID 		INT NOT NULL,
	Department 		VARCHAR(20) NOT NULL,
	Employee 		INT NOT NULL
);


CREATE TABLE Employee (
    	EmployeeID 		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	Name 			VARCHAR(100) NOT NULL,
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
	Name			VARCHAR(30), 
	Preferences		XML
);

CREATE TABLE CustomerTransaction (
	CustomerID		INT NOT NULL PRIMARY KEY,
	TransactionID		INT NOT NULL PRIMARY KEY,
	ShippingAddress		VARCHAR(30),
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
	Cashier			VARCHAR(30) PRIMARY KEY,
	IncomingOrOutgoing	VARCHAR(1) PRIMARY KEY,
	TransactionAmount	DECIMAL(5,2) NOT NULL CHECK (TransactionAmount >= 0)
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
