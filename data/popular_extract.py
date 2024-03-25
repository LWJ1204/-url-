import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_TLD(url):
        # 去除URL中的协议部分（如果有的话）
        if '://' in url:
            url = url.split('://')[1]
            # 按照'.'分割URL部分
        parts = url.split('.')
        # 去除可能的端口号（如果存在）
        if ':' in parts[-1]:
            tld = parts[-1].split(':')[0]  # 假设端口号前的部分是TLD
        else:
            tld = parts[-1]  # 否则，最后一部分就是TLD

        return tld
#世界排名前500
path="E:\jupyter\machine_learning\ml_url\data\popular_web.csv"
path2='E:\jupyter\machine_learning\ml_url\data\china_popular_web.csv'
df1=pd.read_csv(path)
df2=pd.read_csv(path2)
#将中国前1450 和 世界500 拼接在一起，忽略原标签
df=pd.concat([df1,df2],ignore_index=True)
print(df.head())
#去重
url_list=list(set(df['URL']))

#顶级域名
TLD=[]
for url in url_list:
    tempurl=url.lower()
    TLD.append(get_TLD(tempurl))

#提取出现多次的顶级域名
common_TLD=[]
for i in range(0,len(TLD)):
    tempnum=TLD.count(TLD[i])
    if tempnum>=2:
        common_TLD.append(TLD[i])

print(1,set(common_TLD))


#统计流行域名
domain_use_words=[]
index=0
for url in url_list:
    #分组
    tempurl=url
    if '://' in url:
        tempurl = url.split('://')[1]
    url_block=tempurl.split('.')
    url_block.pop(-1)#去掉顶级域名
    for block in url_block:
        if block not in common_TLD:
            domain_use_words.append(block)

text=" ".join(domain_use_words)
wordcloud=WordCloud(
    background_color='white',
    max_words=300,
    random_state=30,
    max_font_size=20,
    scale=15
).generate(text)

plt.imshow(wordcloud)
plt.savefig("popular_cloud.png")
plt.axis('on')
plt.show()
