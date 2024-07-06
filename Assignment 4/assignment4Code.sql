--Database Schema 

--1
CREATE TABLE Product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    brand VARCHAR(100) NOT NULL,
    stock_remaining INT NOT NULL
);

--2
CREATE TABLE Rating (
    rating_id INT PRIMARY KEY AUTO_INCREMENT,
    rating_value INT NOT NULL CHECK (rating_value >= 1 AND rating_value <= 5),
    review TEXT,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

--3
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL
);

--4
CREATE TABLE Order (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    order_date DATETIME NOT NULL,
    user_id INT NOT NULL,
    order_total DECIMAL(10, 2) NOT NULL,
    order_status ENUM('Pending', 'Ordered', 'Shipped', 'Delivered', 'Canceled') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

--5
CREATE TABLE Item (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    quantity INT DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    product_id INT NOT NULL,
    order_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (order_id) REFERENCES Order(order_id)
);

--QUERIES:

--1
SELECT user_id, SUM(order_total) as total_sum
FROM Order
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY user_id
ORDER BY total_sum DESC
LIMIT 3;


--2
SELECT p.product_id, p.name
FROM Product p
LEFT JOIN Item i ON p.product_id = i.product_id
LEFT JOIN `Order` o ON i.order_id = o.order_id
WHERE o.order_date IS NULL OR YEAR(o.order_date) < 2023;

--3
SELECT DISTINCT u.user_id, u.first_name, u.last_name
FROM User u
JOIN Rating r ON u.user_id = r.user_id
LEFT JOIN `Order` o ON u.user_id = o.user_id
LEFT JOIN Item i ON o.order_id = i.order_id
WHERE i.item_id IS NULL;

--4
SELECT YEAR(o.order_date) AS year, p.name AS top_selling_product, SUM(i.quantity) AS total_sold
FROM `Order` o
JOIN Item i ON o.order_id = i.order_id
JOIN Product p ON i.product_id = p.product_id
GROUP BY YEAR(o.order_date)
ORDER BY total_sold DESC;

--5
SELECT p.name AS product_name, AVG(r.rating_value) AS average_rating
FROM Product p
LEFT JOIN Rating r ON p.product_id = r.product_id
GROUP BY p.product_id
ORDER BY average_rating DESC
LIMIT 5;

--6
SELECT p.brand AS brand, SUM(i.quantity) AS total_items_ordered
FROM Product p
JOIN Item i ON p.product_id = i.product_id
JOIN `Order` o ON i.order_id = o.order_id
WHERE YEAR(o.order_date) = 2023
GROUP BY p.brand
ORDER BY total_items_ordered DESC
LIMIT 5;

--7
SELECT u.user_id, u.first_name, u.last_name, 
    (COALESCE(rating_count, 0) + COALESCE(order_count, 0)) AS activity_count
FROM User u
LEFT JOIN (
    SELECT user_id, COUNT(*) AS rating_count
    FROM Rating
    GROUP BY user_id
) AS ratings ON u.user_id = ratings.user_id
LEFT JOIN (
    SELECT user_id, COUNT(*) AS order_count
    FROM `Order`
    GROUP BY user_id
) AS orders ON u.user_id = orders.user_id
ORDER BY activity_count DESC
LIMIT 5;

--8
SELECT p.name AS product_name, COUNT(r.rating_id) AS rating_count
FROM Product p
LEFT JOIN Rating r ON p.product_id = r.product_id
GROUP BY p.product_id
ORDER BY rating_count DESC
LIMIT 10;

--9
SELECT p.brand
FROM Product p
JOIN Rating r ON p.product_id = r.product_id
GROUP BY p.brand
HAVING AVG(r.rating_value) >= 4.0;

--10
SELECT u.user_id, u.first_name, u.last_name,
    COUNT(DISTINCT r.product_id) / COUNT(DISTINCT i.product_id) AS review_proportion
FROM User u
JOIN `Order` o ON u.user_id = o.user_id
LEFT JOIN Item i ON o.order_id = i.order_id
LEFT JOIN Rating r ON u.user_id = r.user_id AND r.product_id = i.product_id
GROUP BY u.user_id
ORDER BY review_proportion DESC
LIMIT 5;
