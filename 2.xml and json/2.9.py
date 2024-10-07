import json

python_dict = {
    "name": "Anh",
    "age": 18,
    "city": "Ha Noi",
    "skills": ["Dev M", "design", "Anything is good"],
    "experience": {
        "company": "Dev Luxury",
        "years": 20
    }
}

data = json.dumps(python_dict)
data_dict = json.loads(data)
print(data)
print('My name is',data_dict['name'],data_dict['age'],'tuổi')
