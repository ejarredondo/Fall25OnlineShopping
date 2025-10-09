DROP SCHEMA IF EXISTS OnlineShopping;
CREATE DATABASE OnlineShopping;
USE OnlineShopping;

CREATE TABLE Supplier(
	SupplierName VARCHAR(255) Unique NOT NULL,
	SupplierID INT Unique PRIMARY KEY AUTO_INCREMENT NOT NULL,
	ItemsSupplied XML,
	NumItems INT,
	StoreAddress VARCHAR(255) Unique NOT NULL,
	STOREID INT,
    FOREIGN KEY (STOREID) REFERENCES Store (StoreID) ON DELETE RESTRICT
);


CREATE TABLE Catalog(
	ProductID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	ProductName VARCHAR(255) NOT NULL,
	Category VARCHAR(255)NOT NULL,	
	SKU INT NOT NULL UNIQUE,
	Weight DECIMAL(5,2),
	BasePrice DECIMAL(7,2) NOT NULL CHECK (BasePrice >= 0),
	SalePrice DECIMAL(7,2),
	DietaryInformation XML,
	SoldByWeightorUnit ENUM('Weight', 'Unit') NOT NULL,
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
    EmployeeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	Name VARCHAR(100) NOT NULL,
	StartDate DATE,
	PayRate DECIMAL(8, 2) CHECK (PayRate >=0) NOT NULL,
	Position VARCHAR(50),
	Availability BOOLEAN,
	BankRoutingInformation VARCHAR(9) NOT NULL,
	CheckingAccountNumber VARCHAR(17) NOT NULL,
	EmailAddress VARCHAR(250)
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
