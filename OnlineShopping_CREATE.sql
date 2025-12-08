DROP DATABASE IF EXISTS OnlineShopping;
CREATE DATABASE OnlineShopping;
USE OnlineShopping;

CREATE TABLE department (
	department_id			INT PRIMARY KEY AUTO_INCREMENT,
	department_name			VARCHAR(20) NOT NULL,
	employee_total			INT NOT NULL
);

CREATE TABLE customer (
	customer_id				INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	first_name				VARCHAR(30),
	last_name				VARCHAR(30)
);

CREATE TABLE employee (
    employee_id              INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name               VARCHAR(100) NOT NULL,
    last_name                VARCHAR(100) NOT NULL,
    start_date               DATE,
    pay_rate                 DECIMAL(8, 2) NOT NULL CHECK (pay_rate >= 0),
    position                 VARCHAR(50),
    availability             BOOLEAN,
    bank_routing_information VARCHAR(9) NOT NULL,
    checking_account_number  VARCHAR(17) NOT NULL,
    email_address            VARCHAR(250)
);

CREATE TABLE catalog (
    product_id               INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    product_name             VARCHAR(255) NOT NULL,
    category                 VARCHAR(255) NOT NULL,
    sku                      INT NOT NULL UNIQUE,
    weight                   DECIMAL(5,2),
    base_price               DECIMAL(7,2) NOT NULL CHECK (base_price >= 0),
    sale_price               DECIMAL(7,2) NOT NULL CHECK (sale_price >= 0),
    sold_by_weight_or_unit   ENUM('weight', 'unit') NOT NULL,
    brand                    VARCHAR(255),
    quantity_of_item         SMALLINT,
    department_id            INT NOT NULL,
    expiration_date          DATE,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE store (
    store_id        INT PRIMARY KEY AUTO_INCREMENT,
    street_address  VARCHAR(30) NOT NULL,
    city            VARCHAR(30) NOT NULL,
    state           VARCHAR(2) NOT NULL,
    zip             VARCHAR(5) NOT NULL
);

CREATE TABLE supplier (
    supplier_id             INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    supplier_name           VARCHAR(255) UNIQUE NOT NULL,
    supplier_address_street VARCHAR(255),
    supplier_address_city   VARCHAR(20),
    supplier_address_state  VARCHAR(2),
    supplier_address_zip    VARCHAR(5),
    store_id                INT,
    FOREIGN KEY (store_id) REFERENCES store(store_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE transaction (
    transaction_id      SMALLINT NOT NULL AUTO_INCREMENT,
    cashier_employee_id INT NOT NULL,
    incoming_or_outgoing ENUM('I', 'O'),
    transaction_amount  DECIMAL(5,2) NOT NULL CHECK (transaction_amount >= 0),
    transaction_date    DATETIME,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (cashier_employee_id) REFERENCES employee(employee_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE ItemSupplied (
    product_id      INT NOT NULL,
    transaction_id  SMALLINT NOT NULL,
    supplier_id     INT NOT NULL,
    store_id        INT NOT NULL,
    item_quantity   SMALLINT NOT NULL,
    PRIMARY KEY (product_id, transaction_id),
    FOREIGN KEY (product_id) REFERENCES catalog(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (store_id) REFERENCES store(store_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE DietaryInformation(
	product_id INT NOT NULL,
    restriction VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES catalog(product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE CustomerPurchaseHistory (
	customer_purchase_history_id	INT AUTO_INCREMENT PRIMARY KEY,
    customer_id		INT NOT NULL,
	transaction_id		SMALLINT NOT NULL,
	amount_spent		DECIMAL(5, 2) NOT NULL,
	date_purchased		DATE,
	time_purchased		TIME,
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (transaction_id) REFERENCES transaction (transaction_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);	

CREATE TABLE CustomerTransaction (
	customer_transaction_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    transaction_id SMALLINT NOT NULL,
    shipping_address_street VARCHAR(30),
    shipping_address_city VARCHAR(30),
    shipping_address_state VARCHAR(2),
    shipping_address_zip VARCHAR(5),
    card_info VARCHAR(30) UNIQUE,
    email_address VARCHAR(30) UNIQUE,
    items_purchased SMALLINT,
    PRIMARY KEY(customer_transaction_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE EmployeeTransaction (
	employee_id			INT NOT NULL,
	transaction_id		SMALLINT NOT NULL,
	store_id			INT NOT NULL,
	PRIMARY KEY( employee_id, transaction_id),
	FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
	FOREIGN KEY (store_id) REFERENCES store(store_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE
);
