import pandas as pd

# Sample dataset — your Phase 1 & 2 lesson scores (made up for practice)
data = {
    "lesson": ["Variables", "Conditionals", "Lists", "Functions", "APIs", "FastAPI"],
    "difficulty": [2, 4, 3, 5, 6, 7],
    "completed": [True, True, True, True, True, True]
}

df = pd.DataFrame(data)

print("Full table:")
print(df)

print("\nAverage difficulty:")
print(df["difficulty"].mean())

print("\nHardest lesson:")
print(df[df["difficulty"] == df["difficulty"].max()])

print("\nSorted by difficulty:")
print(df.sort_values("difficulty"))