import psycopg2

try:
    conn = psycopg2.connect(
        dbname="shopping_bot_dev",
        user="postgres",
        password="Bismillah123",
        host="localhost",
        port="5432"
    )
    print("✅ SUCCESS: Connected!")
except Exception as e:
    print("❌ FAILED:", e)
