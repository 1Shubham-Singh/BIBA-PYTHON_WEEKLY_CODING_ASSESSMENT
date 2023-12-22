import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data)
print(json_data)