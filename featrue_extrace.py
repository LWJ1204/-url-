import torch
import pandas as pd
import numpy as np
import math
import re
import bad_url_extract_features
url_featrue=[
    'URL长度',
    '字母比例',
    '数字比例',
    '特殊符号的种类个数',
    '特殊字符个数',
    'URL深度(/)',
    '出现点的次数(.)',
    '存在@符号',
    '顶级域名TLD',
    '出现恶意词的次数',
    '出现流行网站名的次数',
    '出现.php或者.exe的次数',
    '在除了开头位置出现http,www的次数'
]
path='E:\jupyter\machine_learning\ml_url\data\data.csv'
df=pd.read_csv(path)
url_list=df['url']



#字符串中是否有数字
def contain_digit(str):
    for ch in str:
        if ch.isdigit():
            return True
    return False

def extract_url_feature(url):
    url=url.lower()
    url_len=len(url)

    http_pos=url.find('http://')
    #判断协议是否存在   并且判断http不作为路径部分
    if http_pos!=-1 and http_pos<url.find('/'):
        url=url[http_pos+7:]

    https_pos=url.find('https://')
    if https_pos!=-1 and https_pos<url.find('/'):
        url=url[https_pos+8:]

    www_pos=url.find('www')
    if www_pos!=-1 and www_pos<url.find('.'):
        url=url[www_pos+4:]

    other_pos=url.find('://')
    if other_pos!=-1 and other_pos<url.find('/'):
        url=url[other_pos+4:]

    url_letter_ratio=0#'字母比例',
    url_digit_ratio=0#'数字比例',
    url_kind_fh=0#'特殊符号的种类个数',
    url_num_fh=0#'特殊字符个数',
    url_depth=0#'URL深度(/)',
    url_num_dot=0#'出现点的次数(.)',
    url_at=0#'存在@符号',
    url_TLD=0#'顶级域名TLD',
    url_bad_num=0#'出现恶意词的次数',
    url_popular=0#'出现流行网站名的次数',
    url_php_exe=0#'出现.php或者.exe的次数',
    url_http_www=0#'在除了开头位置出现http,www的次数'

    ch_list=[]#特殊符号

    for i in range(len(url)):
        if url[i].isalpha():
            url_letter_ratio+=1/len(url)
        elif url[i].isdigit():
            url_digit_ratio+=1/len(url)
        elif url[i]=='/':
            url_depth+=1
        elif url[i]=='.':
            url_num_dot+=1
        elif url[i]=='@':
            url_at+=1
        else:
            ch_list.append(url[i])

    url_kind_fh=len(set(ch_list))
    url_num_fh=len(ch_list)

    url_port=80
    parts=url.split('/')
    hostname=parts[0].split('.')
    #print(hostname)
    if contain_digit(hostname[-1])==True:
        tld=hostname[-1].split(':')
        print(tld)
        url_tld_temp=tld[0]
        if len(tld)==2 and  0<int(tld[1])<65535:
            url_port=tld[1]
            #print(url_port,1)
        common_tlds=bad_url_extract_features.common_TLD
        url_TLD=500
        for i in range(len(common_tlds)):
            if common_tlds[i]==url_tld_temp:
                url_TLD=i
                break
    else:
        url_TLD=1000


extract_url_feature('http://example.com:8080/path/to/resource')
#for i in url_list:
    #extract_url_feature(i)