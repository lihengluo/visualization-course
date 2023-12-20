# 搜索百度热搜榜（https://top.baidu.com/board?platform=wise）将前20个热搜词条以词云方式进行展示（热搜排名可以做为字体大小的权重，注意顺序）

from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType

words = [
    ("年轻人报复性挤爆“3.5分饭店", 40),
    ("男子地铁被诬陷偷拍案一审宣判", 38),
    ("“新三样”展现新优势", 36),
    ("周海媚小区保安证实救护车曾来救人", 34),
    ("流感药药店比医院贵百元 多地发文", 32),
    ("一碗30元的网红面馆卖不动了", 30),
    ("2023年流行趋势风格", 28),
    ("降雪能冻死病毒？", 26),
    ("大批空姐转行卖车？多方回应", 24),
    ("女孩回应被男子问5000元玩不玩", 22),
    ("业主欠800万水费 倾家荡产不够交", 20),
    ("小伙定了婚期才知女方一家全是托", 18),
    ("郑爽被强制执行9050万", 16),
    ("万达380亿元对赌危机解除", 14),
    ("谭飞发文辟谣：周海媚并未过世", 12),
    ("巴西球员比赛中被闪电击中身亡", 10),
    ("薛之谦上上谦火锅仅剩两家", 8),
    ("榜一大哥骗走24名家长1000余万元", 6),
    ("研究发现生两个孩子最有利于长寿", 4),
    ("网传周海媚去世最早爆料者删除内容", 2)
]
wordcloud = (WordCloud()
       .add("", words, word_size_range=[10, 30])# word_size_range为字体大小范围
       .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-Baidu Hot 20")) )
wordcloud.render('2-2wordcloud.html')