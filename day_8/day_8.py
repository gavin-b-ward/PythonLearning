dog = {}
dog["name"] = "riley"
dog["color"] = "white with brown spots" 
dog["breed"] = "mixed"
dog["legs"] = 4 
dog["age"] = 12 

student = {
    "first_name": "gavin",
    "last_name": "ward",
    "gender":"male",
    "age": 21,
    "marital_status": "not married",
    "skills": ["programming", "tennis"],
    "country": "US",
    "city": "Atlanta",
    "address": "1123 pp lane",
}

print(len(student))
print(type(student["skills"]))
student["skills"].append("boyfriend")
student["skills"].append("cooking")
print(student)
print(student.keys())
print(student.values())
tpl = student.items()
del student["gender"]
print(student)
del dog

