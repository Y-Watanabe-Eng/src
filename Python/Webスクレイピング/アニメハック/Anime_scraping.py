import requests
from bs4 import BeautifulSoup
import csv

HEADER = ['タイトル', 'URL']

#スクレイピング対象のWEBサイトを指定
res = requests.get('https://anime.eiga.com/program/')

#指定したサイトのHTMLコードを取得
soup = BeautifulSoup(res.text, 'html.parser')

#検索範囲を指定
Container = soup.find('div', class_='animeSeasonContainer')

#pタグのseasonAnimeTtlクラスで囲まれた部位を検索
class_ttl = Container.find_all('p', class_='seasonAnimeTtl')

#CSVファイルの準備
with open('now_anime.csv', 'w', encoding = 'utf-8') as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(HEADER)
    
    for anime in class_ttl:
        #タイトルテキストを取得
        ttl = anime.find('a').text
        #作品URLを取得
        url = anime.find('a').get('href')
        #URLをフルパスに変換
        full_url = 'https://anime.eiga.com' + url

        #CSVに書き出し
        row = [ttl, full_url]
        writer.writerow(row)
        
        #デバッグ用
        print('*************************************************************************************')
        print(ttl)
        print(full_url)
        print('')