# chuyển python sang json
import json
data = '{"name": "Anh", "age": 18, "city": "Ha Noi","company":"Dev luxury"}'
python_obj = json.loads(data)

print(python_obj)
