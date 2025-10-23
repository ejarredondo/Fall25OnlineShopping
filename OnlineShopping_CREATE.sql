CREATE TABLE Supplier(
	SupplierName 		VARCHAR(255) Unique NOT NULL,
	SupplierID 		INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	SupplierAddressCity	VARCHAR(20),
	SupplierAddressState	VARCHAR(2),
	SupplierAddressZip	VARCHAR(5),
	STOREID 		INT,
    	FOREIGN KEY (STOREID) REFERENCES Store (StoreID) 
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);

CREATE TABLE ItemSupplied (
	ProductID		INT NOT NULL,
	TransactionID		INT NOT NULL,	
	SupplierID		INT NOT NULL,
	StoreID			INT NOT NULL,
	ProductName		VARCHAR(255),
	ItemQuantity		SMALLINT NOT NULL,
	PRIMARY KEY( ProductID, TransactionID),
	FOREIGN KEY (ProductID) REFERENCES Catalog (ProductID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (TransactionID) REFERENCES Transaction (TransactionID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (StoreID) REFERENCES Store (StoreID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (ProductName) REFERENCES Catalog (ProductName)
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
	SoldByWeightorUnit 	ENUM('Weight', 'Unit') NOT NULL,
	Brand 			VARCHAR(255),
	QuantityofItem 		SMALLINT
    	DepartmentID 		SMALLINT NOT NULL,
	QuantityofItem 		SMALLINT,
	ExpirationDate		DATE
    	FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
);


CREATE TABLE DietaryInformation(
	ProductID 	INT NOT NULL PRIMARY KEY NOT NULL,
	ProductName 	VARCHAR(255) NOT NULL,
	Restriction 	enum('DairyFree', 'GlutenFree', 'vegetarian', 'vegan', 'kosher', 'keto', 'SugarFree', 'LowCarb', 'PorkFree', 'NutFree', 'ShellfishFree', 'SoyFree'),
	FOREIGN KEY (ProductID) REFERENCES Catalog (ProductID)
    		ON DELETE Restrict
    		ON UPDATE Cascade,
	FOREIGN KEY (ProductName) References Catalog (ProductName)
    		ON DELETE RESTRICT
    		ON UPDATE CASCADE
);

CREATE TABLE Store (
	StoreID 		INT PRIMARY KEY AUTO_INCREMENT,
	StreetAddress 		VARCHAR(30) NOT NULL,
    	City 			VARCHAR(30) NOT NULL,
    	State 			VARCHAR(2) NOT NULL,
    	Zip 			VARCHAR(5) NOT NULL,
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
	PayRate 		DECIMAL(8, 2) NOT NULL CHECK (PayRate >= 0),
	Position 		VARCHAR(50),
	Availability 		BOOLEAN,
	BankRoutingInformation 	VARCHAR(9) NOT NULL,
	CheckingAccountNumber 	VARCHAR(17) NOT NULL,
	EmailAddress 		VARCHAR(250)
);

CREATE TABLE Customer (
	CustomerID		INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FirstName		VARCHAR(30),
	LastName		VARCHAR(30)
);

CREATE TABLE CustomerPurchaseHistory (
	CustomerID		INT NOT NULL,
	TransactionID		INT NOT NULL,
	AmountSpent		DECIMAL(5, 2) NOT NULL,
	DatePurchased		DATE,
	TimePurchased		TIME,
	FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (TransactionID) REFERENCES Transaction (TransactionID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,	
	FOREIGN KEY (AmountSpent) REFERENCES Transaction (TransactionAmount)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (DatePurchased) REFERENCES Transaction (TransactionDate)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);	
	

CREATE TABLE CustomerTransaction (
	CustomerID		INT NOT NULL AUTO_INCREMENT,
	TransactionID		INT NOT NULL AUTO_INCREMENT,
	ShippingAddressStreet	VARCHAR(30),
	ShippingAddressCity	VARCHAR(30),
	ShippingAddressState	VARCHAR(2),
	ShippingAddressZip	VARCHAR(5),
	CardInfo		VARCHAR(30) UNIQUE,
	EmailAddress		VARCHAR(30) UNIQUE,
	TransactionAmount	DECIMAL(5,2) NOT NULL,
	ItemsPurchased		SMALLINT,
	PRIMARY KEY(CustomerID, TransactionID),
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (TransactionAmount) REFERENCES Transaction(TransactionAmount)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);
	
CREATE TABLE Transaction (
	TransactionID		SMALLINT NOT NULL AUTO_INCREMENT,
	CashierEmployeeID	INT NOT NULL,
	IncomingOrOutgoing	ENUM('I', 'O'),
	TransactionAmount	DECIMAL(5,2) NOT NULL CHECK (TransactionAmount >= 0),
	TransactionDate		DATETIME,
	PRIMARY KEY( TransactionID, CashierEmployeeID, IncomingOrOutgoing),
	FOREIGN KEY (CashierEmployeeID) REFERENCES Employee(EmployeeID)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
	
);

CREATE TABLE EmployeeTransaction (
	EmployeeID		SMALLINT NOT NULL,
	TransactionID		SMALLINT NOT NULL,
	StoreID			SMALLINT NOT NULL,
	PRIMARY KEY( EmployeeID, TransactionID),
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
