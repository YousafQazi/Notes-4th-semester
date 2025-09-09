sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
new_dict = {}
for key in keys:
    new_dict[key] = sample_dict[key]
print("\nNEW DICTIONARY:", new_dict)