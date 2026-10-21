import os
import psycopg

print("CI failure test")
print("Python container started")

with open("/run/secrets/db_password", "r") as file:
    db_password = file.read().strip()

connection = psycopg.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=db_password
)

print("Connected to PostgreSQL!")

cursor = connection.cursor()
cursor.execute("SELECT 1;")

result = cursor.fetchone()

print("Database result:", result)

connection.close()
