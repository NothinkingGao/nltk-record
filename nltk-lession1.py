#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

response=urllib.request.urlopen('http://php.net/')
html=response.read()

soup=BeautifulSoup(html,'html5lib')

text=soup.get_text(strip=True)
tokens=text.split()




#去掉停用词
sr = stopwords.words('english')
clean_tokens=[token for token in tokens if token not in sr]

freq=nltk.FreqDist(clean_tokens)

for key,value in freq.items():
	print (str(key)+":"+str(value))

#绘图
freq.plot(20,cumulative=False)
