import pandas as pd

data = {
    "food": ["pizza", "sushi", "tacos"],
    "rating": [9, 7, 8]
}

df = pd.DataFrame(data)
print(df) 
print(df["rating"].mean())
print(df[df["rating"] == df["rating"].max()])
import matplotlib.pyplot as plt

df.plot(x="food", y="rating", kind="bar", legend=False, color="purple")
plt.title("My Food Ratings")
plt.xlabel("Food")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("my_chart.png")
