import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("D:/gean/SQL/BD_SQL_Practicing/Northwind.db")

# Obteniendo los 10 productos más rentables
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

# Lee directamente la consulta y nos da la respuesta. Crea automaticamente el cursor, las conexiones las abre y cierra
top_products = pd.read_sql_query(query, conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar",
                  figsize=(10, 5), legend=False)
plt.title("10 Productos más rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# Obteniendo los 10 empleados más efectivos.
# Se concatena el nombre y el apellido con ||
query2 = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as total 
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY total ASC
    LIMIT 3
'''
top_products2 = pd.read_sql_query(query2, conn)

top_products2.plot(x="Employee", y="total", kind="bar",
                   figsize=(10, 5), legend=False)

plt.title("10 Empleados más efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")
plt.xticks(rotation=45)
plt.show()


# UTILIZANDO WITH.

# Empleados que más recaudaron
