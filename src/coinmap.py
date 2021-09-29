from requests import Request, Session, get
import json

class coin:
    

    def __init__(self):
        pass


    def get_data(self, coin_name):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
        }
        id = self.get_id(coin_name)
        url = f"https://api.coinmarketcap.com/content/v3/news?coins={id}&page=1&size=15"
        request = get(url, headers)
        text = request.json()
        data = text['data']
        coins_news = []
        for n in data:
            if n['meta']:
                meta = n['meta']
                coin_news = []
                coin_news.append(meta['title'])
                coin_news.append(meta['subtitle'])
                coin_news.append(meta['sourceUrl'])
                coins_news.append(coin_news)
        print(coins_news)


    def get_id(self, coin_name):
        headers = {
            'Accepts': 'application/json','X-CMC_PRO_API_KEY': '3de143cc-d878-40d5-8102-30e3d64ebde4',
        }
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        session = Session()
        session.headers.update(headers)
        response = session.get(url)
        data = json.loads(response.text)
        for i in data['data']:
            if i['name']:
                name = i['name']
                if name.upper() == coin_name.upper():
                    return i['id']