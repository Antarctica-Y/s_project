import requests
import json


def getfollow(id):
    user = {}
    DEFAULT_REQUEST_HEADERS = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
       'cookie': '''_uuid=6F62E4F4-AA1D-2536-71085-18BA3D3CCF3C09076infoc; buvid4=E7260CB2-BA1F-F951-CF29-4E7A9791709B07583-022022611-sY8l0EfnQAU7CEcUQivvHg%3D%3D; buvid3=84874592-15DB-F833-9F38-CEDE95ED879807583infoc; b_nut=1645844409; i-wanna-go-back=-1; blackside_state=1; rpdid=|(J|Y||uJmYk0J'uYRY|lJlku; LIVE_BUVID=AUTO1816463137498746; nostalgia_conf=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; DedeUserID=22682736; DedeUserID__ckMd5=b73512ca36f38918; SESSDATA=b8b53fb4%2C1662782883%2C0ef68*31; bili_jct=d6f72503739db19bd727ceb6efcf3e46; CURRENT_QUALITY=80; b_ut=5; sid=c5xbuzbv; buvid_fp=17bdc3ea41f31b5c4b2b9342243de1e2; fingerprint3=d841eca39a61c5218485c2f64a73a152; fingerprint=17bdc3ea41f31b5c4b2b9342243de1e2; hit-dyn-v2=1; is-2022-channel=1; bp_video_offset_22682736=644149905113219100; innersign=0; b_lsid=7101047EE1_17FE80ECC64; CURRENT_FNVAL=80; PVID=1'''
    }
    url = 'https://api.bilibili.com/x/space/upstat?mid=' + str(id)
    r = requests.get(url, headers=DEFAULT_REQUEST_HEADERS)
    r.encoding = r.apparent_encoding
    r_users = json.loads(r.text)['data']
    user['view_num'] = r_users['archive']['view']
    user['like_num'] = r_users['likes']
    return user

getfollow(2)