import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm
import matplotlib.dates as mdates

# 读取 excel 文件
data_history = pd.read_excel("dataset/covid19_data.xls", sheet_name="data_history")

# 设置中文标注
fm.findfont(fm.FontProperties(fname="Microsoft Yahei"))
plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]

plt.rcParams["axes.unicode_minus"] = False

# Converting 'date' column to datetime format
data_history['date'] = pd.to_datetime(data_history['date'])

# Plotting line and scatter plots
fig, ax = plt.subplots(2, 1, figsize=(12, 12))

# Line plot
ax[0].plot(data_history['date'], data_history['confirm'], label='Confirmed', color='blue', linestyle='-')
ax[0].plot(data_history['date'], data_history['dead'], label='Deaths', color='red', linestyle='--')
ax[0].plot(data_history['date'], data_history['heal'], label='Recovered', color='green', linestyle='-.')

# Scatter plot
ax[1].scatter(data_history['date'], data_history['confirm'], label='Confirmed', color='blue')
ax[1].scatter(data_history['date'], data_history['dead'], label='Deaths', color='red')
ax[1].scatter(data_history['date'], data_history['heal'], label='Recovered', color='green')

# Setting titles and labels
ax[0].set_title('COVID-19 Data Over Time (Line Plot)', fontsize=14)
ax[1].set_title('COVID-19 Data Over Time (Scatter Plot)', fontsize=14)
for a in ax:
    a.set_xlabel('Date', fontsize=12)
    a.set_ylabel('Number of Cases', fontsize=12)
    a.legend()
    a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    a.xaxis.set_major_locator(mdates.MonthLocator())
    a.tick_params(axis='x', rotation=45)
    a.set_xticks(data_history['date'])




# Adjusting layout for readability
plt.tight_layout()

# Show plot
plt.savefig("res/1-1.png")