import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm

# 读取 excel 文件
data_world = pd.read_excel("dataset/covid19_data.xls", sheet_name="data_world")

# 设置中文标注
fm.findfont(fm.FontProperties(fname="Microsoft Yahei"))
plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]

plt.rcParams["axes.unicode_minus"] = False


# Selecting the top 4 countries based on confirmed cases
top_countries = data_world.nlargest(4, 'confirm')

# Creating a pie chart for each of the top 4 countries to show the distribution of confirm, dead, heal, and suspect
fig, axes = plt.subplots(2, 2, figsize=(14, 14))
axes = axes.flatten()  # Flatten the axes array for easy indexing

# Loop through the top 4 countries and plot pie charts
for i, (index, row) in enumerate(top_countries.iterrows()):
    labels = ['Confirm', 'Dead', 'Heal', 'Suspect']
    sizes = [row['confirm'], row['dead'], row['heal'], row['suspect']]
    axes[i].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[i].set_title(f'COVID-19 Distribution in {row["country"]}', fontsize=14)

# Adjusting layout for better visualization
plt.tight_layout()

# Show plot
plt.savefig("res/1-2.png")