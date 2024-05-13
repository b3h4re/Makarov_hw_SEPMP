import mysql.connector as mysql, os
from datetime import date


name = "test_db"
db = mysql.connect(host="localhost", user="root", passwd="password", database=name)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
for database in cursor.fetchall():
    if name == database[0]:
        break
else:
    cursor.execute(f"CREATE DATABASE {name}")

cursor.execute("SHOW TABLES")
table_name = "users"
for table in cursor.fetchall():
    if table_name == table[0]:
        break
else:
    print("zklscnsdljvnsldvnklsdvnksdnvlsdknvk")
    cursor.execute("CREATE TABLE users "
                   "(ord_no integer, perch_amt float, ord_date date, customer_id integer, salesman_id integer)")


cursor.execute(f"DESC {table_name}")
print(cursor.fetchall())

query = "INSERT INTO users (ord_no, perch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
values_list = [
    (1, 150.5, date(year=2012, month=9, day=5), 5+300, 2+500),
    (2, 270.65, date(year=2012, month=9, day=10), 2+300, 5+500),
    (3, 123.23, date(year=2012, month=9, day=11), 3+300, 9+500),
    (4, 656.50, date(year=2012, month=9, day=12), 1+300, 7+500),
    (5, 334.00, date(year=2012, month=9, day=13), 8+300, 4+500),
    (6, 234.00, date(year=2012, month=9, day=14), 9+300, 5+500),
    (7, 24.10, date(year=2012, month=9, day=15), 3+300, 2+500),
    (8, 44.11, date(year=2012, month=9, day=16), 2+300, 1+500),
    (9, 20.50, date(year=2012, month=9, day=17), 7+300, 1+500),
    (10, 1.00, date(year=2012, month=9, day=20), 5+300, 1+500)
]


cursor.executemany(query, values_list)

salesman_id = 502
query = f"SELECT ord_no, ord_date, perch_amt FROM {table_name} WHERE salesman_id = {salesman_id}"
cursor.execute(query)

print(f"for salesman_id = {salesman_id}:")
for row in cursor.fetchall():
    print(f"    order number: {row[0]}, date: {row[1].year}-{row[1].month}-{row[1].day}, amount purchased: {row[2]}")

print("\n" + '--' * 15 + "\n")

query = f"SELECT DISTINCT salesman_id FROM {table_name}"
cursor.execute(query)
unique_ids = []
for ids in cursor.fetchall():
    unique_ids.append(ids[0])
print(unique_ids)

print("\n" + '--' * 15 + "\n")

query = f"SELECT ord_date, salesman_id, ord_no, perch_amt FROM {table_name}"
cursor.execute(query)
for order in cursor.fetchall():
    print(order)

print("\n" + '--' * 15 + "\n")
start = 1
end = 7

query = f"SELECT * FROM {table_name} WHERE ord_no BETWEEN {start} AND {end}"
cursor.execute(query)
for order in cursor.fetchall():
    print(order)