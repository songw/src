import jieba
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud  # 词云包

my_list = []
comments = ""
with open("./my_sister.txt", 'r') as f:
    for line in f.readlines():
        comments += line.strip()

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filter_data = re.findall(pattern, comments)
cleaned_comments = ''.join(filter_data)

segment = jieba.lcut(cleaned_comments)
words_df = pd.DataFrame({'segment': segment})

stopwords = pd.read_csv("stopwords.txt", index_col=False,
                        quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat = words_df.groupby('segment').agg(计数=pd.NamedAgg(column='segment', aggfunc='size')).reset_index() \
    .sort_values(by='计数', ascending=False)

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

wc = WordCloud(font_path="/System/Library/fonts/PingFang.ttc",
               width=1200, height=600)
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

word_cloud = wc.generate_from_frequencies(word_frequence)
plt.imshow(word_cloud)
word_cloud.to_file('my_sister.png')
