import redis
import psycopg2
import json

# PostgreSQL connection
pg_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)
pg_cursor = pg_conn.cursor()

# Redis connection
cache = redis.Redis(host='localhost', port=6379, db=0)

def get_data(query, cache_key, expire_time=300):
    # Check cache first
    if cache.exists(cache_key):
        print("Fetching from Redis cache...")
        return json.loads(cache.get(cache_key))
    
    # Query PostgreSQL
    print("Fetching from PostgreSQL...")
    pg_cursor.execute(query)
    rows = pg_cursor.fetchall()
    
    # Store result in Redis
    cache.setex(cache_key, expire_time, json.dumps(rows))
    return rows

# Example Usage
query = "SELECT * FROM customers ;"
data = get_data(query, cache_key="employees_IT")
print(data)