
def folder_make(name):
    try:
        if not os.path.exists(name):
            os.makedirs(name)
            print(f"Directory{name} is created")
    except:
        print("Failed to create directory!!!!!")


def save_search_image(imgs,max_count):
    count=0
    del imgs[0]#delet useless info
    for i in imgs:
        count += 1
        if count < max_count + 1:
            full_name = str(keyword) + '_' + str(count) + ".jpg"
            urllib.request.urlretrieve(i.get('src'), full_name)
            print(f"=========[{count}/{max_count} success]========+ ")
    print("Download completed!!")


def get_count(num,p): #how many process do you need == p
    list=[]
    allocate=int(num/p)
    for n in range(p):
        list.append(allocate)
    list[p-1]+=num%p # 마지막은 남는거 다
    return list



import multiprocessing
import requests
from lxml.html import parse
from io import StringIO
import os
import time
import urllib






if __name__=="__main__":

    # keyword = input("검색할 이미지를 입력하세요 : ")
    keyword = '계란'
    max_count= 13
    url = 'https://www.google.co.kr/search?q=' + keyword + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'

    # html 소스 가져오기
    text = requests.get(url).text

    # html 문서로 파싱
    text_source = StringIO(text)
    parsed = parse(text_source)

    # root node
    doc = parsed.getroot()

    imgs = doc.findall('.//img')  # img 경로는 img 태그안에 src에 있음(20개만 크롤링 됨.. 이유 찾아봐야 됨)
    # search_image(keyword)

    #make directory and change path
    folder_make(str(keyword))
    currentPath = os.getcwd() # get current path
    changePath = currentPath + '/' + str(keyword) #make change path
    os.chdir(changePath) # change path


    #strat multiprocessing
    num=int(max_count)
    t0=time.time()
    process=[]

    for count in get_count(num,6):
        p=multiprocessing.Process(target=save_search_image,args=(imgs,max_count))
        process.append(p)
        p.start()

    #pause untill multiprocessing finished
    for p in process:
        p.join()

    t1=time.time()
    print("End Crawling")
    print("Amount time: ",round(t1-t0,4))





