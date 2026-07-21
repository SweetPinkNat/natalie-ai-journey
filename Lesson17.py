import pandas as pd
import matplotlib.pyplot as plt

data = {
    "lesson": ["Variables", "Conditionals", "Lists", "Functions", "APIs", "FastAPI", "Pandas"],
    "difficulty": [2, 4, 3, 5, 6, 7, 6]
}
df = pd.DataFrame(data)

# Bar chart
df.plot(x="lesson", y="difficulty", kind="bar", legend=False, color="purple")
plt.title("My Python Journey — Lesson Difficulty")
plt.xlabel("Lesson")
plt.ylabel("Difficulty (1-10)")
plt.tight_layout()
plt.show()