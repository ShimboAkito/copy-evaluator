import time
import re
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

url1='https://www.tcc.gr.jp/copira/?count=20&copy&copywriter&ad&biz&media&start&end&target_prize=all'
# max_page = 1757
valid_media = {'新聞','ポスター', '雑誌', 'パンフレット', 'その他'}
with open('./data/slogans.tsv', 'w') as f:
    print('full_copy', 'short_copy', 'company', 'award', 'sector', 'media', 'writer', 'year', 'page', 'product', 'url', sep='\t', file=f)
    r = requests.get(url1)
    soup = BeautifulSoup(r.content, 'html.parser')
    max_page = int(re.findall(r'(\d*)', soup.find('p', class_='block9__result').text)[0])//20+1
    copies = soup.find_all('p',class_='')
    medium = soup.find_all('td',class_='text-align-right')
    for i in range(20):
        if medium[i].text.strip('\n') in valid_media:
            time.sleep(1)
            company = award = sector = media = writer = year = page = ''
            individual_url = soup.find_all('p', class_='')[i].find_all('a')[0]['href']
            individual_request = requests.get(individual_url)
            individual_soup = BeautifulSoup(individual_request.content, 'html.parser')
            full_text = individual_soup.find('p', class_='block5-1__catch').text
            full_text = re.sub('\s\s+', ' ', full_text.strip(r"'\r\n").replace(r'\n', ' ').replace('\n', ' ').replace(r'\u3000', ' '))
            short_text = soup.find_all('p', class_='')[i].text
            short_text = re.sub('\s\s+', ' ', short_text.strip(r"'\r\n").replace(r'\n', ' ').replace('\n',' ').replace(r'\u3000', ' '))
            note = individual_soup.find('p', class_='block5-1__notes').text
            table_rows = individual_soup.find_all('tr')
            for row in table_rows:
                th = row.find('th').text
                td = row.find('td').text.replace('\n', '')
                if td == '':
                    td = 'None'
                if th=='広告主':
                    company = td
                elif th=='受賞':
                    award = td
                elif th=='業種':
                    sector = td
                elif th=='媒体':
                    media = td
                elif th=='コピーライター':
                    writer = td
                elif th=='掲載年度':
                    year = td
                elif th=='掲載ページ':
                    page = td
            if award=='' or award == None:
                award = 'None'
            if note == '' or note == None:
                note = 'None'
            print(repr(full_text.strip('\n')), repr(short_text.strip('\n')), company.replace('\t', ''), award.replace('\t',''), sector.replace('\t',''), media.replace('\t',''), writer.replace('\t',''), year.replace('\t',''), page.replace('\t',''), note.strip('\n').replace('\n',' '), individual_url, sep='\t', file=f)
    
    for p in tqdm(range(2,max_page+1)):
        r = requests.get('https://www.tcc.gr.jp/copira/page/'+str(p)+'/?count=20&copy&copywriter&ad&biz&media&start&end&target_prize=all')
        soup = BeautifulSoup(r.content, 'html.parser')
        copies = soup.find_all('p',class_='')
        medium = soup.find_all('td',class_='text-align-right')
        for i in range(len(copies)):
            if medium[i].text.strip('\n') in valid_media:
                company = award = sector = media = writer = year = page = ''
                time.sleep(1)
                individual_url = soup.find_all('p', class_='')[i].find_all('a')[0]['href']
                individual_request = requests.get(individual_url)
                individual_soup = BeautifulSoup(individual_request.content, 'html.parser')
                full_text = individual_soup.find('p', class_='block5-1__catch').text
                full_text = re.sub('\s\s+', ' ', full_text.strip(r"'\r\n").replace(r'\n', ' ').replace('\n', ' ').replace(r'\u3000', ' '))
                short_text = soup.find_all('p', class_='')[i].text
                short_text = re.sub('\s\s+', ' ', short_text.strip(r"'\r\n").replace(r'\n', ' ').replace('\n', ' ').replace(r'\u3000', ' '))
                note = individual_soup.find('p', class_='block5-1__notes').text
                table_rows = individual_soup.find_all('tr')
                for row in table_rows:
                    th = row.find('th').text
                    td = row.find('td').text
                    if td == '':
                        td = 'None'
                    td = td.replace('\n', '')
                    if th=='広告主':
                        company = td
                    elif th=='受賞':
                        award = td
                    elif th=='業種':
                        sector = td
                    elif th=='媒体':
                        media = td
                    elif th=='コピーライター':
                        writer = td
                    elif th=='掲載年度':
                        year = td
                    elif th=='掲載ページ':
                        page = td
                if award == '':
                    award = 'None'
                if note == '':
                    note = 'None'
                print(repr(full_text.strip('\n')), repr(short_text.strip('\n')), company.replace('\t',''), award.replace('\t',''), sector.replace('\t',''), media.replace('\t',''), writer.replace('\t',''), year.replace('\t',''), page.replace('\t',''), note.strip('\n').replace('\n', ''), individual_url, sep='\t', file=f)
        