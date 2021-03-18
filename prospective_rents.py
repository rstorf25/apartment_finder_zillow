import requests
from bs4 import BeautifulSoup
import json
import time
import csv


class rentScraper():
    results = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en - US, en;q = 0.9',
        'cache-control': 'max-age=0',
        'cookie': 'zguid=23|%242de3976a-7e4a-4bd1-ae26-b9263d3965b8; _ga=GA1.2.502546616.1615319976; zjs_user_id=null; zjs_anonymous_id=%222de3976a-7e4a-4bd1-ae26-b9263d3965b8%22; _gcl_au=1.1.2078943761.1615319976; _pxvid=f8d4c292-8111-11eb-8e59-0242ac120005; _pin_unauth=dWlkPU9ETXlOemczWm1JdFptRTVZUzAwT0dVeExUazRaakl0TW1NME1EVmlOV0UxTlRndw; _fbp=fb.1.1615319976725.510967309; __gads=ID=2c01c31dbe87fd54:T=1615319981:S=ALNI_MayZGsFd8HyL_dBqwwHzj7i7AJOQg; ki_r=; ki_s=; ki_t=1615320089783%3B1615320089783%3B1615320097925%3B1%3B5; zgcus_aeut=AEUUT_fb8930ce-834b-11eb-b430-9611b9b263ae; zgcus_aeuut=AEUUT_fb8930ce-834b-11eb-b430-9611b9b263ae; optimizelyEndUserId=oeu1615564794466r0.9957253480622619; FSsampler=724764527; _cs_c=1; _cs_id=f99ccc4d-392f-a361-d13a-8b889c6db96a.1615564796.1.1615564796.1615564796.1.1649728796928.Lax.0; __CT_Data=gpv=1&ckp=tld&dm=zillow.com&apv_82_www33=1&cpv_82_www33=1; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+12+2021+09%3A59%3A57+GMT-0600+(Central+Standard+Time)&version=5.11.0&landingPath=https%3A%2F%2Fwww.zillow.com%2Frental-manager%2F%3Fsource%3Dtopnav%26itc%3Dpostbutton_sitenav&groups=1%3A1%2C3%3A1%2C4%3A1; __stripe_mid=176caf89-7737-4b1e-bb96-af36415f3f0e15023e; _gac_UA-21174015-56=1.1615566692.Cj0KCQiAv6yCBhCLARIsABqJTjbOa4GYyOYOGRJElKB4ZGxiB_ps5DNZG5BMtosoI0FexxkQQ-85AdwaAmI_EALw_wcB; _gcl_aw=GCL.1615566692.Cj0KCQiAv6yCBhCLARIsABqJTjbOa4GYyOYOGRJElKB4ZGxiB_ps5DNZG5BMtosoI0FexxkQQ-85AdwaAmI_EALw_wcB; _gid=GA1.2.1019772380.1615821275; KruxPixel=true; g_state={"i_p":1615919030728,"i_l":2}; zgsession=1|c527be7b-245b-48a6-80ea-7fb9577dac43; JSESSIONID=7A8A046D457FB394218A037BE1DAAC79; DoubleClickSession=true; _derived_epik=dj0yJnU9S1h5b2ZJM0QyZldreG1fV29Ec05FMDg1ektaUXRDNkQmbj0ya25aOVc4R0VrNTBCVm1MM0RpQVFRJm09NyZ0PUFBQUFBR0JRNWNvJnJtPWUmcnQ9QUFBQUFHQkxrTEU; _uetsid=28e3435085a111eb950e69e75cb8ad7d; _uetvid=f946c500811111ebaba9b91bc30631aa; _px3=07dc2b451a233a67a3e291b8ff4ecefcdbd13016296c6f563496d0773cd97a80:2ybEi9Zfuh6chPkBIOGpiB7tXCd+OlgcJ/oN0/1CegnBfzyUfi+hxW2ThhVu8kXNxn5wxQf6JSw/B78qZ4TJ4A==:1000:lWdPIN1DbB+zd71oPdHBsejCn7dBEKWalgWztmORxHtTuQuSpDYwohShVfwa+/TVXW7X2fWjdxEmWk6qFoDSqiaXsF8qHHHBhMRCQlB1VRwna/m6YcJMurYJomk16ZmidXJ2wwb4BSO7MPWMlp0fZjc4e/kQZrdEdPhYGjh6H6o=; KruxAddition=true; AWSALB=w+0Lg+4TwDl9Mcnavozsp5Kx0Q2z3tTg29cQPvbeUd4lOHY2yZabW5/1XjV+R0/DfVq5Atu1oFwynhTAn2d4MR3F8u4U0nSWanD9mgH8pxipQE3w5W/15aUXJ5lK; AWSALBCORS=w+0Lg+4TwDl9Mcnavozsp5Kx0Q2z3tTg29cQPvbeUd4lOHY2yZabW5/1XjV+R0/DfVq5Atu1oFwynhTAn2d4MR3F8u4U0nSWanD9mgH8pxipQE3w5W/15aUXJ5lK; search=6|1618506542628%7Crect%3D42.236997020793275%252C-87.39753041530493%252C41.41630492644361%252C-89.00428090358618%26crid%3D925126050eX1-CR1s0kvahwa2ri_w6us6%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0913650%09%09%09%09%09%09',
        'referer': 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-88.62799916530493%2C%22east%22%3A-87.77381215358618%2C%22south%22%3A41.41630492644361%2C%22north%22%3A42.236997020793275%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22customRegionId%22%3A%22925126050eX1-CR1s0kvahwa2ri_w6us6%22%7D',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    def fetch(self, url, params):
        response = requests.get(url, headers=self.headers, params=params)
        print(response.status_code)
        return response

    def parse(self, response):
        content = BeautifulSoup(response, 'lxml')
        deck = content.find('ul', class_='photo-cards photo-cards_wow photo-cards_short')
        for card in deck:
            script = card.find('script', {'type': 'application/ld+json'})
            article = card.find('article', {'class': 'list-card list-card-additional-attribution list-card_not-saved list-card_building'})
            if script:
                script_json = json.loads(script.contents[0])

                self.results.append({
                    'address': script_json['name'],
                    'type': script_json['@type'],
                    'price': card.find('div', class_='list-card-price').text,
                    'details': card.find('ul', class_='list-card-details').text,
                    # 'lat': script_json['geo']['latitude'],
                    # 'long': script_json['geo']['longitude'],
                    'url': script_json['url']
                }
                )
            elif article:

                self.results.append({
                    'address': card.find('address', class_='list-card-addr').text,
                    'type': card.find('abbr', class_='list-card-label').text,
                    'price': card.find('div', class_='list-card-price').text,
                    'details': card.find('abbr', class_='list-card-label').text,
                    'url': """https://www.zillow.com/homedetails/{}""".format(card.find('address', class_='list-card-addr').text).replace(" ","-").replace("|","-").replace(",","")
                })



    def to_csv(self):
        with open('personal_search_317.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()

            for row in self.results:
                writer.writerow(row)

    def run(self):
        url = 'https://www.zillow.com/homes/Chicago,-IL_rb/'
        for page in range(1, 20):
            params = {
                'searchQueryState': '{"pagination":{"currentPage": %s},"mapBounds":{"west":-88.69735036159399,"east":-87.70446095729712,"south":41.41630492644361,"north":42.236997020793275},"customRegionId":"925126050eX1-CR1s0kvahwa2ri_w6us6","isMapVisible":false,"filterState":{"pmf":{"value":false},"fore":{"value":false},"ah":{"value":true},"auc":{"value":false},"nc":{"value":false},"fr":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"pf":{"value":false},"fsba":{"value":false}},"isListVisible":true}' % page
            }
            res = self.fetch(url, params)
            self.parse(res.text)
            time.sleep(2)
        self.to_csv()


if __name__ == '__main__':
    scrapper = rentScraper()
    scrapper.run()
