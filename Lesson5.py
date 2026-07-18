# Creating a dictionary
pet = {
    "name": "Max",
    "type": "dog",
    "age": 3
}

print(pet)
print(pet["name"])
print(pet["type"])

# Modifying
pet["age"] = 4
print(pet)

pet["breed"] = "labrador"
print(pet)

del pet["type"]
print(pet)

# Looping
for key, value in pet.items():
    print(f"{key}: {value}")