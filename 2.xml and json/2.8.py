import json 
data = {"name": "Anh",
         "age": 18, 
         "city": "Ha Noi",
         "company":"Dev luxury"}
json_data = json.dumps(data)
print(json_data)
