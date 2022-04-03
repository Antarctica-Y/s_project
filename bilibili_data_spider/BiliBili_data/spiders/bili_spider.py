import scrapy
import json
from .Getfollow import getfollow
import re

class BiliSpiderSpider(scrapy.Spider):
    name = 'bili_spider'

    custom_settings = {
        'DOWNLOAD_DELAY':0.6
    }
    def start_requests(self):
        for i in range(2467, 10001):
            url1 = 'https://api.bilibili.com/x/space/acc/info?mid='
            url2 = 'https://api.bilibili.com/x/space/bangumi/follow/list?vmid='
            url3 = 'https://api.bilibili.com/x/space/navnum?mid='
            url4 = 'https://api.bilibili.com/x/relation/stat?vmid='
            url5 = 'https://api.bilibili.com/x/space/upstat?mid='
            newUrl1 = url1 + str(i)
            yield scrapy.http.Request(newUrl1, callback=self.parse)
            newUrl2 = url2 + str(i) + '&type=1'
            yield scrapy.http.Request(newUrl2, callback=self.parse2)
            newUrl3 = url3 + str(i)
            yield scrapy.http.Request(newUrl3, callback=self.parse3)
            newUrl4 = url4 + str(i)
            yield scrapy.http.Request(newUrl4, callback=self.parse4)
            # newUrl5 = url5 + str(i) + '&jsonp=jsonp'
            # yield scrapy.http.Request(newUrl5, callback=self.parse5)


    def parse(self, response):
        json_users = json.loads(response.text)['data']
        user = {}
        tagg = ''
        user = getfollow(json_users['mid'])
        user['id'] = json_users['mid']
        user['name'] = json_users['name']
        if json_users['birthday'] != '':
            user['birthday'] ='0-' + json_users['birthday']
        else:
            user['birthday'] = None
        user['level'] = json_users['level']
        user['off_title'] = json_users['official']['title']
        if json_users['school'] != None:
            user['sch_name'] = json_users['school']['name']
        user['sex'] = json_users['sex']
        user['sign'] = json_users['sign']

        if json_users['tags'] != None:
            for tag in json_users['tags']:
                if tag != json_users['tags'][-1]:
                    tagg = tagg + tag + '&&'
                else:
                    tagg = tagg + tag
        user['tag'] = tagg
        user['vip'] = json_users['vip']['label']['text']
        yield user

    def parse2(self, response):
        json_users = json.loads(response.text)
        user = {}
        user['id'] = int(re.findall(r'\d+', response.url)[0])
        if json_users['message'] != '用户隐私设置未公开':
            user['tot_cartoon'] = json_users['data']['total']
        yield user

    def parse3(self, response):
        json_users = json.loads(response.text)['data']
        user = {}
        user['id'] = int(re.findall(r'\d+', response.url)[0])
        user['album'] = json_users['album']
        user['article'] = json_users['article']
        user['audio'] = json_users['audio']
        user['video'] = json_users['video']
        yield user

    def parse4(self, response):
        json_users = json.loads(response.text)['data']
        user = {}
        user['id'] = int(re.findall(r'\d+', response.url)[0])
        user['follower'] = json_users['follower']
        user['following'] = json_users['following']
        yield user

    # def parse5(self, response):
    #     json_users = json.loads(response.text)['data']
    #     user = {}
    #     user['id'] = int(re.findall(r'\d+', response.url)[0])
    #     user['view_num'] = json_users['archive']['view']
    #     user['like_num'] = json_users['likes']
    #     yield user

