import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#popular_extract.py 生成
common_TLD=[
    'hk', 'nl', 'ru', 'edu', 'org', 'gov', 'eu',
    'co', 'me', 'ch', 'es', 'ly', 'tv', 'io',
    'us', 'de', 'net', 'fr', 'jp', 'in', 'ca',
    'cc', 'la', 'cn', 'au', 'uk', 'br', 'pl','com'
]

path='E:\\jupyter\\machine_learning\\ml_url\\data\\bad_urls.csv'
df=pd.read_csv(path,header=None)
df.columns=['URL',"Lable"]
bad_url=list(set(df['URL']))

bad_text=""
def conunt_common_bad_words():
    global bad_text
    bad_word=[]
    for url in bad_url:
        #将url进行分割
        url_block=re.split('[-_/&.()<>^@!#$*=+~:;? ]',url)
        while '' in url_block:
            url_block.remove('')
        #提取恶意url中不属于常见顶级域名的内容
        for tempurl in url_block:
            if tempurl not  in common_TLD:
                bad_word.append(tempurl)
    bad_text=''.join(bad_word)
    bad_words=pd.DataFrame(data=bad_word,columns=['words'])
    words_bag=bad_words['words'].value_counts()#统计每种bad word出现次数
    words_bag_index=words_bag.index #提取标签

    bad_word_in_url=[]
    for i in range(len(words_bag)):
        if words_bag[i]>5:
            word=words_bag_index[i]
            if 2<len(word)<25:
                bad_word_in_url.append(word)
    bad_word_df=pd.DataFrame(data=bad_word_in_url,columns=['word'],index=None)
    bad_word_df.to_csv('bad_word.csv')

def draw_bad_word():
    wordcloud=WordCloud(
        background_color='white',
        max_words=300,
        random_state=30,
        max_font_size=20,
        scale=20
    ).generate(bad_text)
    plt.imshow(wordcloud)
    plt.savefig('bad_word.png')
    plt.axis('off')
    plt.show()

#conunt_common_bad_words()
#draw_bad_word()
