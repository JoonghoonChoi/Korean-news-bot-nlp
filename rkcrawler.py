import requests
from bs4 import BeautifulSoup


def rknews_crwaler(n_news):
    print('뉴스를 가져오는 중입니다...')
    # n_news: 불러 올 뉴스 기사 수
    base_url= "https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111"
    headers = {'User-Agent': 'Mozilla/5.0'} # 403에러가 뜰 때 헤더를 추가해주면 접근할 수 있음
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print(response.status_code)

    news_url_lst = []

    info = soup.findAll('div', {'class': 'list_content'})
    for each in info:
        each_news = each.findAll('a', {'class': "list_title nclicks('RBP.rnknws')"})
        news_url = 'https://news.naver.com/' + each_news[0].get('href')
        news_url_lst.append(news_url)

    text_lst = []

    for news_url in news_url_lst[:n_news]: # 크롤링해올 뉴스 개수
        res_article= requests.get(news_url, headers=headers)

        if res_article.status_code == 200:
            html_article = res_article.text
            soup_article = BeautifulSoup(html_article, 'html.parser')
        else : 
            print(res_article.status_code)

        text = soup_article.findAll('div', {'class':'_article_body_contents'})[0].text

        if text == []:
            continue

        # if '▶' in text:
        #     try:
        #         text = text.split('▶')[:-5][0]
        #     except IndexError:
        #         pass

        text = ' '.join(text.split('\n')[8:])
        text = '.'.join(text.split('.')[:-2])
        text_lst.append(text)
    
    print(f'실시간 랭킹 뉴스 {len(text_lst)}개를 가져왔습니다.')
    return text_lst