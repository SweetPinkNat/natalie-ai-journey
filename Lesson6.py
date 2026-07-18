# Writing to a file
with open("journal.txt", "w") as file:
    file.write("Today I learned file handling in Python!")

# Reading it back
with open("journal.txt", "r") as file:
    content = file.read()
    print(content)

# Appending more
with open("journal.txt", "a") as file:
    file.write("\nThis is my 6th script.")

# Reading again to confirm the append worked
with open("journal.txt", "r") as file:
    content = file.read()
    print(content)