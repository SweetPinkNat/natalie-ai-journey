# Creating a list
foods = ["pizza", "sushi", "tacos"]

print(foods)
print(foods[0])
print(foods[-1])
print(len(foods))

# Modifying
foods.append("pasta")
print(foods)

foods[1] = "ramen"
print(foods)

foods.remove("tacos")
print(foods)

# Looping
for food in foods:
    print(f"I like {food}")
    