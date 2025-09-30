CREATE TABLE Store (
	StoreID INT,
	Address VARCHAR(30) NOT NULL,
	Inventory XML,
	DepartmentID INT NOT NULL,
	Department VARCHAR(20) NOT NULL,
	Employee INT NOT NULL,
	PRIMARY KEY (StoreID)
);
