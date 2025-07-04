use SalesDB
-- Muestra el nombre completo de los clientes y el nombre de los productos que han comprado.

SELECT 
	c.FirstName,
	c.LastName,
	p.Product

FROM Sales.Customers AS c
INNER JOIN Sales.OrdersArchive AS o
ON o.CustomerID = c.CustomerID
INNER JOIN Sales.Products AS p
ON o.ProductID = p.ProductID

-- Muestra el nombre completo del cliente, el nombre del producto y la cantidad comprada.

SELECT 
	c.FirstName,
	c.LastName,
	p.Product,
	o.Quantity

FROM Sales.Customers AS c
INNER JOIN Sales.OrdersArchive AS o
ON o.CustomerID = c.CustomerID
INNER JOIN Sales.Products AS p
ON o.ProductID = p.ProductID

-- Mostrar todos los productos disponibles, incluso si nunca fueron vendidos

SELECT
	Product,
	'Unsold' AS Sales 
FROM Sales.Products AS p
LEFT JOIN Sales.Orders AS o
ON o.ProductID= p.ProductID
WHERE OrderID IS NULL

-- Mostrar cuántos productos distintos ha comprado cada cliente.

SELECT
	CustomerID,
	COUNT(DISTINCT ProductID) AS Product_Quantity
FROM Sales.Orders AS o
GROUP BY o.CustomerID

/* Mostrar todos los empleados que han vendido productos, junto con el total de 
ventas que generaron */


SELECT
	SalesPersonID,
	FirstName,
	SUM(Sales) AS Total_Sales
FROM Sales.Orders AS o
INNER JOIN Sales.Employees AS e
ON o.SalesPersonID = e.EmployeeID
GROUP BY o.SalesPersonID, e.FirstName

/* Muestra el nombre del producto y la cantidad total vendida de cada uno. */

SELECT
	o.ProductID,
	p.Product,
	SUM(Quantity) AS Total_Quantity
FROM Sales.Products AS p
INNER JOIN Sales.OrdersArchive AS o
ON o.ProductID = p.ProductID
GROUP BY o.ProductID, p.Product

/* Mostrar el pais del cliente y la cantidad total de ventas generadas por país. */

SELECT 
	--c.CustomerID,
	--c.FirstName,
	c.Country,
	SUM(Quantity) AS Total_QuantitybyCountry
FROM Sales.Customers AS c
INNER JOIN Sales.Orders AS o
ON o.CustomerID = c.CustomerID
GROUP BY c.Country --c.CustomerID, --c.FirstName

/* Muestra los productos vendidos, ordenados por la cantidad total vendida de 
mayor a menor. */

SELECT
	o.ProductID,
	p.Product,
	SUM(Quantity) AS Total_Quantity
FROM Sales.Products AS p
INNER JOIN Sales.Orders AS o
ON o.ProductID = p.ProductID
GROUP BY o.ProductID, p.Product
ORDER BY SUM(Quantity) DESC

/* Muestra los nombres de todos los clientes que no han realizado ningún pedido. */

SELECT
	FirstName,
	LastName
FROM Sales.Customers AS c
lEFT JOIN Sales.Orders AS o
ON o.CustomerID = c.CustomerID
WHERE o.OrderID IS NULL


/* Muestra todos los clientes y productos, incluso si el cliente no ha comprado 
nada o el producto nunca fue vendido. */

SELECT
	c.FirstName,
	c.LastName,
	p.Product
FROM Sales.Customers AS c
FULL JOIN Sales.Orders AS o
ON o.CustomerID = c.CustomerID
left JOIN Sales.Products AS p
ON o.ProductID = p.ProductID;

/* Muestra el nombre del producto y el número total de veces que fue vendido 
(sin importar la cantidad por pedido). */

SELECT
	o.ProductID,
	p.Product,
	COUNT(o.ProductID) AS Total_vecesVendido
FROM Sales.Products AS p
INNER JOIN Sales.Orders AS o
ON o.ProductID = p.ProductID
GROUP BY o.ProductID, p.Product


/* Muestra una lista combinada de todos los países de los clientes y todos 
los países de los empleados, sin duplicados. */

SELECT
	Country
FROM Sales.Customers AS c
INNER JOIN Sales.Orders AS o
ON o.CustomerID = c.CustomerID

UNION

SELECT
	Country
FROM Sales.Employees AS e
INNER JOIN Sales.Orders AS o
ON o.SalesPersonID = e.EmployeeID
