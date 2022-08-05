import MeCab
import re 
text = open('./rss28.txt', 'r', encoding='UTF-8').read()
mecab = MeCab.Tagger('-d C:/MeCab/dic/NEologd')
res = mecab.parseToNode(text)

meisi=[] 
k_meisi=[]

while res:
    arr = res.feature.split(",")
    
    pattern=re.findall("(?<=\「).+?(?=\」)", text)
    kakko="\n".join(pattern) 
    if (arr[0] == "名詞"):
        meisi.append(arr[6])
        if(arr[1] == "固有名詞"):
            if(arr[6]=="*"):
                k_meisi.append("")
            else:
                k_meisi.append(arr[6])
                k_meisi_unique=list(dict.fromkeys(k_meisi))
                string="\n".join(k_meisi_unique)
    res = res.next
 
with open('rss_unique_result.txt', 'w', encoding='UTF-8') as f: 
       f.writelines(string)
       f.writelines(kakko)

str1 =""

with open('rss_unique_result.txt', 'r', encoding='UTF-8') as f:
    unique_texts = {line.rstrip() for line in f}

for i in unique_texts:
    str1 += i+"\n"

with open('result' + '.disticted.txt', 'a', encoding='UTF-8') as f:
    f.writelines(str1)
