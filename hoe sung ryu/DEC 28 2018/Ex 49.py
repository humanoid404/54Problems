
def folder_make(name):
    try:
        if not os.path.exists(name):
            os.makedirs(name)
            print(f"Directory{name} is created")
    except:
        print("Failed to create directory!!!!!")




import time
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib
# from urllib.request import urlopen

# keyword = input("검색할 이미지를 입력하세요 : ")
keyword='계란'

folder_make(str(keyword))

#get current path
currentPath = os.getcwd()
changePath=currentPath+'/'+str(keyword)
#change path
os.chdir(changePath)

url = 'https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'

 # html 소스 가져오기
text = requests.get(url).text

# html 문서로 파싱
text_source = StringIO(text)
parsed = parse(text_source)

# root node
doc = parsed.getroot()

imgs = doc.findall('.//img')# img 경로는 img 태그안에 src에 있음(20개만 크롤링 됨.. 이유 찾아봐야 됨)
del imgs[0] #delet useless info
count=0
max_count=13

t0 = time.time()
for i in imgs:
    count+=1
    if count < max_count+1:
        full_name=str(keyword)+'_'+str(count)+".jpg"
        urllib.request.urlretrieve(i.get('src'),full_name)
        print(f"[image {count} sucess]============= ")

t1=time.time()
print("Download completed!!")
print("Amount time: ",round(t1-t0,4))
