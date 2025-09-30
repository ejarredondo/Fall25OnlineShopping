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


