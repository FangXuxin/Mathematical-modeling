'''
Time : 2022/1/17 12:32 
File : PlayerUrl.py 
'''
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def get_single_url(datalist,datadic,baseurl):
    if datalist == []:
        print("开始爬取！")
        driver = init_driver()
        driver.get(baseurl)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for k in soup.find_all('div', {'class': 'player'}):
            name = k.find('a').get_text()
            datalist.append(name[1:-1])
            playerUrl = k.find('a')['href']
            datadic.update({name[1:-1]: playerUrl})
        driver.close()
        print('完成爬取！')

    count = 0
    for name in datalist:
        datadic[name] = datadic[name] + '/tournament-results'
        print('完成第 %d 个fin_url的爬取！' % (count+1))
        count += 1
    print('爬取完毕！')

def get_double_url(datalist,datadic,baseurl):
    if datalist == []:
        print("开始爬取！")
        driver = init_driver()
        driver.get(baseurl)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        temp = 0; Name = []; Dic = {}
        for k in soup.find_all('div', {'class': 'player'}):
            if temp <= 1:
                name = k.find('a').get_text()
                playerUrl = k.find('a')['href']
                list(name)
                Dic[name[1:-1]] = playerUrl
                Name.append(name[1:-1])
                temp += 1
            else:
                datalist.append(Name)
                datadic.append(Dic)
                temp = 1
                Name = []; Dic = {}
                name = k.find('a').get_text()
                playerUrl = k.find('a')['href']
                list(name)
                Dic[name[1:-1]] = playerUrl
                Name.append(name[1:-1])
        driver.close()
    # print(datadic)
    print('完成爬取！')

    n = 0
    for item in datalist:
        count = 0
        for i in item:
            if count < 2:
                datadic[n][i] = datadic[n][i] + '/tournament-results'
            else: break
            count += 1
        print('完成第 %d 组的爬取！' % (n+1))
        n += 1

    print('爬取完毕！')
    # print(datadic)

def init_driver():
    option = webdriver.EdgeOptions()
    option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    option.add_argument('headless')
    driver = webdriver.Edge(
        r'C:\Users\Allen\AppData\Local\Programs\Python\Python39\edgedriver_win64\msedgedriver.exe',
        options=option)
    return driver

def saveDate(path, filename, data):
    print("开始保存！")
    ad = path + filename + '.txt'
    js = json.dumps(data)
    fn = open(ad, 'w')
    fn.write(js)
    fn.close()
    print("已保存！")

def readData(path):
    fn = open(path, 'r')
    js = fn.read()
    dic = json.loads(js)
    return dic


def main():
    # https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=57&ryear=2021&week=48&page_size=100&page_no=1
    # https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=58&ryear=2021&week=48&page_size=100&page_no=1
    # https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=59&ryear=2021&week=48&page_size=100&page_no=1
    # https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=60&ryear=2021&week=48&page_size=100&page_no=1
    # https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=61&ryear=2021&week=48&page_size=100&page_no=1

    ms_name, ws_name = [], []
    md_name, wd_name, mind_name = [], [], []

    MS, WS = {}, {}
    MD, WD, MIXD = [], [], []
    MSurl = 'https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=57&ryear=2021&week=48&page_size=100&page_no=1'
    WSurl = 'https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=58&ryear=2021&week=48&page_size=100&page_no=1'
    MDurl = 'https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=59&ryear=2021&week=48&page_size=100&page_no=1'
    WDurl = 'https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=60&ryear=2021&week=48&page_size=100&page_no=1'
    MISDurl = 'https://bwfworldtourfinals.bwfbadminton.com/rankings/?id=9&cat_id=61&ryear=2021&week=48&page_size=100&page_no=1'

    path = 'D:\py_project\\bishe+shixun\shixun\\data\\'

    get_single_url(ms_name,MS,MSurl)
    saveDate(path, 'MS_url', MS)

    get_single_url(ws_name,WS,WSurl)
    saveDate(path, 'WS_url', WS)

    get_double_url(md_name,MD,MDurl)
    saveDate(path, 'MD_url', MD)

    get_double_url(wd_name,WD,WDurl)
    saveDate(path, 'WD_url', WD)

    get_double_url(mind_name,MIXD,MISDurl)
    saveDate(path, 'MIXD_url',MIXD)



if __name__ == '__main__':
    main()