import psycopg2
import json

# Connection parameters 
connection_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user': 'postgres',
    'password': 'password',
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

# Execute a query to fetch data from the user_table
query = "SELECT user_id, name, age, phone FROM user_table;"
cursor.execute(query)
results = cursor.fetchall()

# Convert the results to JSON format
data = []
for row in results:
    user_id, name, age, phone = row
    user_data = {
        'user_id': user_id,
        'name': name,
        'age': age,
        'phone': phone,
    }
    data.append(user_data)

# Construct the JSON response
response = {
    'status_code': 200,
    'data': data,
}

# Convert the response to a JSON string
json_string = json.dumps(response)

# Print the JSON string
print(json_string)

# Close the cursor and connection
cursor.close()
conn.close()
