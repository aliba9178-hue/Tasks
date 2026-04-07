import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Softlaptop\Downloads\students_small.csv")

print(data.head())

print(data.info())

print(data.describe())

plt.scatter(data["Study_Hours"], data["Final_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.show()


plt.boxplot(data["Final_Score"])
plt.title("Final Score Boxplot")
plt.show()
