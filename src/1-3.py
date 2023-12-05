import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm

# 读取 excel 文件
current_prov = pd.read_excel("dataset/covid19_data.xls", sheet_name="current_prov")

# 设置中文标注
fm.findfont(fm.FontProperties(fname="Microsoft Yahei"))
plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]

plt.rcParams["axes.unicode_minus"] = False

# 利用直方图和条形图绘制excel文件中current_prov对应的数据（各省新冠疫情数据），要求使用多个子图
# Setting the positions and width for the bars
provinces = current_prov["province"]
positions = np.arange(len(provinces))
width = 0.25
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Draw the histogram using bar
axes[0].bar(positions, current_prov['confirm'], width, color='blue')
axes[0].set_title('Histogram of Confirmed Cases by Province', fontsize=14)
axes[0].set_xlabel('Province', fontsize=12)
axes[0].set_ylabel('Number of Confirmed Cases', fontsize=12)
axes[0].set_xticks(positions)
axes[0].set_xticklabels(provinces, rotation=45)

# Plotting each category
axes[1].bar(positions - width, current_prov['confirm'], width, label='Confirmed', color='blue')
axes[1].bar(positions, current_prov['dead'], width, label='Dead', color='red')
axes[1].bar(positions + width, current_prov['heal'], width, label='Healed', color='green')

# Adding labels and title
axes[1].set_title('Bar Chart of Confirmed Cases by Province', fontsize=14)
axes[1].set_xlabel('Province', fontsize=12)
axes[1].set_ylabel('Number of Confirmed Cases', fontsize=12)
axes[1].set_xticks(positions)
axes[1].set_xticklabels(provinces, rotation=45)

axes[1].legend()

plt.tight_layout()

# Show plot
plt.savefig("res/1-3.png")
