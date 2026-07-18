# for loop with range
for i in range(5):
    print(i)

print("---")

# for loop with start and stop
for i in range(2, 7):
    print(i)

print("---")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

print("---")

# break example
for i in range(10):
    if i == 5:
        break
    print(i)

print("---")

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)