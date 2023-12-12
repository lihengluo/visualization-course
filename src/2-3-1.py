import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line, Page

# Load the data
file_path = '../dataset/student.xls'
data = pd.read_excel(file_path)

# clean the data, if the value is str or null, set it to 0
data = data.fillna(0)
for subject in ['英语', '体育', '军训', '数分', '高代', '解几']:
    data[subject] = data[subject].apply(lambda x: 0 if isinstance(x, str) else x)

data['总分'] = data[['英语', '体育', '军训', '数分', '高代', '解几']].sum(axis=1)

# 1. Bar Chart for Total Scores
bar = Bar()
bar.add_xaxis(data['姓名'].tolist())
bar.add_yaxis("英语", data['英语'].tolist())
bar.add_yaxis("体育", data['体育'].tolist())
bar.add_yaxis("军训", data['军训'].tolist())
bar.add_yaxis("数分", data['数分'].tolist())
bar.add_yaxis("高代", data['高代'].tolist())
bar.add_yaxis("解几", data['解几'].tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title="Total Scores of All Students"),
                    toolbox_opts=opts.ToolboxOpts(),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45))
                    )

# 2. Pie Chart for Top 3 Students
top_students = data.nlargest(3, '总分')
page = Page()
for _, student in top_students.iterrows():
    pie = Pie()
    scores = [student['英语'], student['体育'], student['军训'], student['数分'], student['高代'], student['解几']]
    pie.add(student['姓名'], list(zip(['英语', '体育', '军训', '数分', '高代', '解几'], scores)))
    pie.set_global_opts(title_opts=opts.TitleOpts(title=f"Top 3 Student {student['姓名']}"))
    page.add(pie)

# 3. Line Chart for Score Distribution
line = Line()
for subject in ['英语', '体育', '军训', '数分', '高代', '解几']:
    hist, bin_edges = np.histogram(data[subject], bins=range(0, 101, 10))
    line.add_xaxis([f'{int(bin_edges[i])}-{int(bin_edges[i+1])}' for i in range(len(bin_edges)-1)])
    line.add_yaxis(subject, hist.tolist())
    line.set_global_opts(toolbox_opts=opts.ToolboxOpts())

# 4. Comparison of Average Scores
average_scores = data.groupby('性别')[['英语', '体育', '军训', '数分', '高代', '解几']].mean().round(2).T
bar_gender = Bar()
bar_gender.add_xaxis(average_scores.index.tolist())
for gender in average_scores.columns:
    bar_gender.add_yaxis(gender, average_scores[gender].tolist())

# Rendering the charts (you can also save them as HTML files)
bar.render("../res/2-3-1bar.html")
page.render("../res/2-3-2pie.html")
line.render("../res/2-3-3line.html")
bar_gender.render("../res/2-3-4bar_gen.html")
