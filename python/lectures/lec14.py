'''A dictionary is a mutable, unordered collection of key-value pairs in Python.'''
student = {
    "name": "Antrares",
    "age": 20,
    "courses": ["Math", "Physics"]
}




info = {"name": "Alice"}
print(info["name"]) 
print(info.get("age", "Not Found"))


info["city"] = "Delhi"     # Add new key
info["name"] = "Bob"       # Update value


info.update({"name": "Charlie", "gender": "Male"})


for key in info:
    print(key)

for key, value in info.items():
    print(f"{key} -> {value}")

'''nested'''
students = {
    "101": {"name": "Ravi", "marks": 88},
    "102": {"name": "Sita", "marks": 91}
}
print(students["101"]["name"])  # Ravi




squares = {x: x*x for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, ...}



text = "apple"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)  # {'a': 1, 'p': 2, 'l': 1, 'e': 1}




def all_positive(d):

    result = []
    for key, value_list in d.items():
        if sum(value_list) > 0:
            result.append(key)
    return sorted(result)

d = {5: [2, -4], 2: [1, 2, 3], 1: [2]}

print(all_positive(d))  
