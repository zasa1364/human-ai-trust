import pandas as pd
import matplotlib.pyplot as plt

# خواندن دیتاست
df = pd.read_csv("datasets/trust_data.csv")

# چاپ چند خط اول برای اطمینان
print(df.head())

# رسم نمودار اعتماد انسان
plt.plot(df["time_step"], df["human_trust_level"])
plt.xlabel("Time Step")
plt.ylabel("Human Trust Level")
plt.title("Human Trust in AI over Time")
plt.grid(True)

# ذخیره نمودار
plt.savefig("trust_plot.png")

print("Plot saved as trust_plot.png")
