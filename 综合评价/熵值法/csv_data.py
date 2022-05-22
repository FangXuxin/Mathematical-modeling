'''
Time : 2022/1/17 14:53 
File : csv_data.py
'''
import json
import urllib.request
from selenium import webdriver
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

def load_data(filename):
    path = 'D:\py_project\\bishe+shixun\shixun\\data\\' + filename + '.txt'
    fn = open(path, 'r')
    js = fn.read()
    data = json.loads(js)
    return data

def grab_web(baseurl):
    driver = init_driver()
    driver.get(baseurl)
    html = driver.page_source

    return html

def get_data(data):
    # 获得单打球员信息
    if type(data) == type({}):
        fin_record = [];name = []
        count = 1
        for k,v in data.items():
            name.append(k)
            player_year_sum = [0,0,0]
            for year in range(2017,2022):
                baseurl = v + '/?year=' + str(year)
                html = grab_web(baseurl)
                soup = BeautifulSoup(html, 'html.parser')
                record = [];temp_record = []

                try:
                    for k in soup.find_all('div', {'class':'player-result-win'}):
                        temp_record.append(k.find('strong').get_text())
                    record.append(temp_record.count('W'))
                    record.append(temp_record.count('L'))
                    record.append(temp_record.count('-'))
                    player_year_sum = np.sum([player_year_sum,record],axis=0).tolist()
                except Exception as result:
                    record = [0,0,0]
                    player_year_sum = np.sum([player_year_sum,record],axis=0).tolist()
                print('-'*50)
                print(record)
                print('完成第 %d 位运动员 %d 战绩爬取！' % (count,year))
            fin_record.append(player_year_sum)
            print('完成第 %d 位运动员 2017-2022 年战绩爬取' % count,player_year_sum)
            count += 1

        df = pd.DataFrame(fin_record,index=name,columns=['Win','Lose','-'])
        return df

    else:   # 获得双打球员的信息
        fin_record = []; team_name = []
        count = 1
        for li in data:
            team = list(li.keys())
            team_name.append(team)
            player_year_sum = [0,0,0]
            for year in range(2017,2022):
                baseurl = li[team[0]] + '/?year=' + str(year)
                html = grab_web(baseurl)
                soup = BeautifulSoup(html, 'html.parser')
                record = []; temp_record = []

                try:
                    for n in soup.find_all('div', {'class': 'tournament-matches-row'}):
                        name = []
                        for k in n.find_all('div', {'class': 'player-result-name-1'}):
                            for i in k.find_all('a'):
                                name.append(i.get_text()[1:-1])
                            if name == team:
                                temp_record.append(n.find('strong').get_text())
                    record.append(temp_record.count('W'))
                    record.append(temp_record.count('L'))
                    record.append(temp_record.count('-'))
                    player_year_sum = np.sum([player_year_sum, record], axis=0).tolist()
                except Exception as result:
                    record = [0, 0, 0]
                    player_year_sum = np.sum([player_year_sum, record], axis=0).tolist()
                print('-'*50)
                print(record)
                print('完成第 %d 队运动员 %d 战绩爬取！' % (count,year))
            fin_record.append(player_year_sum)
            print('完成第 %d 队运动员 2017-2022 年战绩爬取' % count, player_year_sum)
            count += 1
            # print(team_name,fin_record)

        indexs =[]
        for i in team_name:
            indexs.append(i[0] + ' & ' + i[1])
        df = pd.DataFrame(fin_record, index=indexs, columns=['Win', 'Lose', '-'])
        return df


def init_driver():
    option = webdriver.EdgeOptions()
    option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    option.add_argument('headless')
    driver = webdriver.Edge(
        r'C:\Users\Allen\AppData\Local\Programs\Python\Python39\edgedriver_win64\msedgedriver.exe',
        options=option)
    return driver

def save_to_csv(path, filename, data):
    Path = path + filename + '.csv'
    data.to_csv(Path,encoding='utf-8')  # -sig
    print(filename + '保存成功！')


def main():
    path = 'D:\py_project\\bishe+shixun\shixun\csv_data\\'
    # 获取单个运动员的输赢数据
    # MS, WS, MD, WD, MIXD = {}, {}, {}, {}, {}
    MS = load_data('MS_url')
    WS = load_data('WS_url')
    MD = load_data('MD_url')
    WD = load_data('WD_url')
    MIXD = load_data('MIXD_url')
    print(MS); print(WS); print(MD); print(WD); print(MIXD)

    save_to_csv(path,'MS',get_data(MS))
    save_to_csv(path,'WS',get_data(WS))
    save_to_csv(path,'MD',get_data(MD))
    save_to_csv(path,'WD',get_data(WD))
    save_to_csv(path,'MIXD',get_data(MIXD))

    # 保存至excle
    # save_to_excle()


if __name__ ==  '__main__':
    main()