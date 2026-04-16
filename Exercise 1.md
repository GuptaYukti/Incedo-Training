thevarungupta5@gmail.com





Exercise 1:



\-- Create Customers table

CREATE TABLE Customers (

&#x20;   CustomerID INT PRIMARY KEY,

&#x20;   Name VARCHAR(100),

&#x20;   City VARCHAR(100)

);



\-- Create Orders table

CREATE TABLE Orders (

&#x20;   OrderID INT PRIMARY KEY,

&#x20;   CustomerID INT,

&#x20;   OrderDate DATE,

&#x20;   Amount DECIMAL(10, 2),

&#x20;   FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)

);





\-- Insert into Customers

INSERT INTO Customers VALUES 

(1, 'Alice', 'New York'),

(2, 'Bob', 'Chicago'),

(3, 'Charlie', 'Los Angeles'),

(4, 'David', 'Miami');



\-- Insert into Orders

INSERT INTO Orders VALUES 

(101, 1, '2024-07-01', 250.00),

(102, 2, '2024-07-03', 450.00),

(103, 1, '2024-07-04', 300.00),

(104, 3, '2024-07-05', 150.00);





Task 1: Get all customers who have placed at least one order

SELECT C.CUSTOMERID, COUNT(\*)

FROM ORDERS O JOIN CUSTOMERS C

ON C.CUSTOMERID = O.CUSTOMERID

GROUP BY C.CUSTOMERID

HAVING COUNT(\*)>=1



Task 2: List all orders with customer name and city

SELECT O.\* , C.NAME, C.CITY

FROM ORDERS O JOIN CUSTOMERS C

ON C.CUSTOMERID = O.CUSTOMERID





Task 3: Get total order amount for each customer

SELECT C.CUSTOMERID, SUM(AMOUNT)

FROM ORDERS O JOIN CUSTOMERS C

ON C.CUSTOMERID = O.CUSTOMERID

GROUP BY C.CUSTOMERID



















\# Exercise 2: 



\-- Create Departments Table

CREATE TABLE departments (

&#x20;   dept\_id INT PRIMARY KEY,

&#x20;   dept\_name VARCHAR(50)

);



\-- Create Employees Table

CREATE TABLE employees (

&#x20;   emp\_id INT PRIMARY KEY,

&#x20;   emp\_name VARCHAR(50),

&#x20;   salary DECIMAL(10,2),

&#x20;   dept\_id INT,

&#x20;   manager\_id INT

);



\-- Insert Departments

INSERT INTO departments VALUES

(1, 'Engineering'),

(2, 'Marketing'),

(3, 'Sales');



\-- Insert Employees

INSERT INTO employees VALUES

(101, 'Alice', 80000, 1, NULL),

(102, 'Bob', 60000, 1, 101),

(103, 'Charlie', 50000, 2, 101),

(104, 'David', 40000, NULL, NULL),

(105, 'Eve', 75000, 3, 103),

(106, 'Frank', 30000, 2, 103);







Task 1: List all employees with their department names. (INNER JOIN)

SELECT E.EMPID, D.DEP\_ID, D.DEP\_NAME

FROM EMPLOYEE E JOIN DEPARTMENT D 

ON E.DEPTID = OD.DEPTID





Task 2: Show all employees and their departments. Also show employees without a department. (LEFT JOIN)

SELECT E.EMPID, D.DEP\_ID, D.DEP\_NAME

FROM EMPLOYEE E LEFT JOIN DEPARTMENT D 

ON E.DEPTID = D.DEPTID





Task 3: Show all departments and employees. Include departments with no employees. (RIGHT JOIN)

SELECT E.EMPID, D.DEP\_ID, D.DEP\_NAME

FROM EMPLOYEE E RIGHT JOIN DEPARTMENT D 

ON E.DEPTID = OD.DEPTID





Task 4: Show all employees and departments, including unmatched ones from both sides. (FULL JOIN)

SELECT E.EMPID, D.DEP\_ID, D.DEP\_NAME

FROM EMPLOYEE E FULL JOIN DEPARTMENT D 

ON E.DEPTID = OD.DEPTID





Task 5: Display each employee and their manager's name. (SELF JOIN)

SELECT E.EMP\_NAME AS EMPLOYEE, M.EMP\_NAME AS MANAGER

FROM EMPLOYEE E JOIN EMPLOYEE M 

ON E.MANAGER\_ID = M.EMPID





Task 6: Highest Paid Employee Per Department

SELECT E.EMPID, E.EMP\_NAME, D.DEP\_ID, E.SALARY

FROM (

&#x09;SELECT E.\*, D.\*,

&#x09;DENSE\_RANK() OVER (PARTITION BY D.DEPTID ORDER BY E.SALARY DESC) AS RNK

&#x09;FROM EMPLOYEE E JOIN DEPARTMENT D 

&#x09;ON E.DEPTID = OD.DEPTID

&#x20;    ) T

WHERE T.RNK = 1











Exercise 3: 



\-- Create Departments Table

CREATE TABLE departments (

&#x20;   dept\_id INT PRIMARY KEY,

&#x20;   dept\_name VARCHAR(50)

);



\-- Create Employees Table

CREATE TABLE employees (

&#x20;   emp\_id INT PRIMARY KEY,

&#x20;   emp\_name VARCHAR(50),

&#x20;   salary DECIMAL(10,2),

&#x20;   dept\_id INT,

&#x20;   manager\_id INT

);



\-- Create Projects Table

CREATE TABLE projects (

&#x20;   project\_id INT PRIMARY KEY,

&#x20;   project\_name VARCHAR(50),

&#x20;   dept\_id INT

);





\-- Departments

INSERT INTO departments VALUES

(1, 'Engineering'),

(2, 'Marketing'),

(3, 'Sales'),

(4, 'HR');



\-- Employees

INSERT INTO employees VALUES

(101, 'Alice', 80000, 1, NULL),

(102, 'Bob', 60000, 1, 101),

(103, 'Charlie', 50000, 2, 101),

(104, 'David', 40000, NULL, NULL),

(105, 'Eve', 75000, 3, 103),

(106, 'Frank', 30000, 2, 103);



\-- Projects

INSERT INTO projects VALUES

(201, 'Website Revamp', 1),

(202, 'Ad Campaign', 2),

(203, 'Client Outreach', 3),

(204, 'Hiring Drive', 4),

(205, 'Data Migration', 1);









Task 5: Display each employee along with their manager’s name.

SELECT E.EMP\_NAME AS EMPLOYEE, M.EMP\_NAME AS MANAGER

FROM EMPLOYEE E JOIN EMPLOYEE M 

ON E.MANAGER\_ID = M.EMPID



Task 6: List all projects with their department name and employees working in that department.

SELECT P.PROJECT\_ID, P.PROJECT\_NAME, D.DEP\_NAME, E.EMP\_ID, E.EMP\_NAME

FROM PROJECT P

JOIN DEPARTMENT D ON P.DEPTID = D.DEPTID

JOIN EMPLOYEE E ON D.DEPTID = E.DEPTID



Task 7: List employees who do not belong to a department that has a project.

SELECT E.EMP\_ID, E.EMP\_NAME

FROM EMPLOYEE E

LEFT JOIN DEPARTMENT D ON E.DEPTID = D.DEPTID

JOIN PROJECT P ON D.DEPTID = P.DEPTID

WHERE D.DEPTID IS NULL





Task 8: Find all departments that are handling more than one project and display the department name with the number of project

SELECT D.DEPT\_ID, D.DEP\_NAME, COUNT(P.PROJECT\_ID)

FROM PROJECT P

JOIN DEPARTMENT D ON P.DEPTID = D.DEPTID

GROUP BY D.DEPT\_ID, D.DEP\_NAME

HAVING COUNT(P.PROJECT\_ID)>1





Task 9: Show the highest paid employee in each department along with the department’s project(s).

SELECT E.EMPID, E.EMP\_NAME, D.DEP\_ID, E.SALARY, P.PROJECT\_NAME

FROM (

&#x09;SELECT E.\*, D.\*, P.PROJECT\_NAME,

&#x09;DENSE\_RANK() OVER (PARTITION BY D.DEPTID ORDER BY E.SALARY DESC) AS RNK

&#x09;FROM EMPLOYEE E 

&#x09;JOIN DEPARTMENT D ON E.DEPTID = OD.DEPTID

&#x09;JOIN PROJECT P ON D.DEPTID = P.DEPTID

&#x20;    ) T

WHERE T.RNK = 1





Task 10: List each employee, their manager, and the department both belong to.

SELECT E.EMP\_NAME AS EMPLOYEE, M.EMP\_NAME AS MANAGER

FROM EMPLOYEE E 

JOIN EMPLOYEE M ON E.MANAGER\_ID = M.EMPID

JOIN DEPARTMENT D ON E.DEPTID = D.DEPTID

WHERE E.DEPTID = M.DEPTID



Task 11: Create all possible combinations of employees and projects (even if unrelated).

SELECT P.PROJECT\_ID, P.PROJECT\_NAME, D.DEP\_NAME, E.EMP\_ID, E.EMP\_NAME

FROM EMPLOYEE E 

CROSS JOIN PROJECT P

LEFT JOIN DEPARTMENT D1 ON E.DEPTID = D1.DEPTID

LEFT JOIN DEPARTMENT D2 ON P.DEPTID = D2.DEPTID





Task 12: Department Summary Report

For each department, show:

\- Department name

\- Number of employees

\- Number of projects

\- Average salary





SELECT D.DEPT\_ID, D.DEP\_NAME, COUNT(E.EMP\_ID) AS EMPLOYEES, COUNT(P.PROJECT\_ID) AS PROJECTS, AVG(E.SALARY)

FROM DEPARTMENT D

JOIN PROJECT P ON D.DEPTID = E.DEPTID

JOIN EMPLOYEE E ON D.DEPTID = E.DEPTID

GROUP BY D.DEPT\_ID, D.DEP\_NAME







