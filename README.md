
# This repository contains LeetCode solutions and certain learnings on the way forward...!!!


## Learnings

### SQL

1. Add below two lines in the gitattributes to include SQL in the language statistics.

	*.sql linguist-language=sql
	
	*.sql linguist-detectable=true

2. auto_increment in MySQL is similar to Identity() in SQL-Server.
3. Constraint naming inline to column declaration is not permissible in MySQL

```
Create Table Products
(product_id int Constraint PK_Products Primary Key Identity(1,1),
product_name varchar(100),
product_category varchar(50))
```
The above is a valid query in SQL-Server whereas in MySQL it becomes

```
Create Table Products
(product_id int Primary Key auto_increment,
product_name varchar(100),
product_category varchar(50));
```

4. Foreign key declaration for MySQL can only be done at the end of table declaration

```
Create Table Orders
(product_id int ,
order_date date,
unit int,
FOREIGN KEY (product_id) REFERENCES Products(product_id));
```

5. While inserting values into another table with foreign key constraints, MySQL throws an error until setting the below line.

```
SET FOREIGN_KEY_CHECKS=0;
```

6. Even for auto_increment, need to mention the column names the values being inserted

```
insert into Products (product_name, product_category) values
('Leetcode Solutions', 'Book'),
('Jewels of Stringology', 'Book'),
('HP', 'Laptop'),
('Lenovo', 'Laptop'),
('Leetcode Kit', 'T-shirt');
```

7. Wildcard characters like [], -, ^ does not work in MySQL. Instead one can use 'regexp' keyword for a pattern matching in the query in MySQL. Here is an example

```
select * from Users
where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$';
```

8. Similar to ISNULL(expr, value) in SQL-Server, MySQL has IFNULL(expr, value) function that can return a specific value if the expression is NULL.

### Python

1. say nums[] is an existing list. Now, nums[:] means creating a new list as nums but it is a not the same object but a different one.
2. O(logn) is common complexity, where there is a concept of halving or say to perform some action on next element based on some conditions.
3. int(n, 2) base 2 to convert to integer from binary.
4. := is a valid operator that allows assignment of variable within expressions.