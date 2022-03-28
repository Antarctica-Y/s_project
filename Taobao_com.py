import requests
import re

def getHTMLText(url):
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52",
        "cookie":"t=6fb15472e7eeab57abd6b9c49c3600d4; cna=MFieGrF7ZFQCAbZkGCVs0f2w; _m_h5_tk=f408c82cd73f5b23b2458eff286707c8_1648378309835; _m_h5_tk_enc=53e25cece2847dc1dba2a3cb37990b01; xlly_s=1; _samesite_flag_=true; cookie2=1c5f070f6eca4e6067f0a5829d6b15b4; _tb_token_=3ee1bee5e6e8b; sgcookie=E100GZ95lgyEzlBpSXclrDSt3UI42dzlXxT2VziK6wdc9g3KOd2wlj0IOjCEHjPy7EZNtgPn2xHY5sfh3XRdXuDPclpPIw33%2BZHzCwkVnmLDOVPuuEQk889rCVSELAxs4NHn; unb=3303508165; uc1=cookie21=UtASsssme%2BBq&existShop=false&cookie14=UoewCLKtxpgONg%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=kIuqJ8uERZI%3D&id2=UNN9dgdz0i74dQ%3D%3D&vt3=F8dCvCop%2Fgk0zKEnoVQ%3D; csg=5ab0d2f9; lgc=%5Cu7B71%5Cu6768%5Cu4E3666; cancelledSubSites=empty; cookie17=UNN9dgdz0i74dQ%3D%3D; dnk=%5Cu7B71%5Cu6768%5Cu4E3666; skt=9d04b04003b36b90; existShop=MTY0ODM2OTM0MA%3D%3D; uc4=id4=0%40UgQ1KBA8K8mAXekHnZyjXfoybLui&nk4=0%40koD%2BC9aJtJJ4oZ8aDezaIAcYoQ%3D%3D; tracknick=%5Cu7B71%5Cu6768%5Cu4E3666; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=651; _nk_=%5Cu7B71%5Cu6768%5Cu4E3666; cookie1=ACrndmcD8v5Jd%2FcW7oYPHwD2stGohjcASs6PcgwyaLw%3D; enc=WjVtyJVl4nOjFdOmfIFwhfplVxcMIH1uruknV2E37PaVpzMaNQ0jnV%2F5DmAgksUDQITorXlyhu1jmqp1hLsAZQ%3D%3D; x5sec=7b227365617263686170703b32223a22623865326339636364663635613637313666643266356139303234393066633843504459674a4947454a763175386e78386f2f7052686f4d4d7a4d774d7a55774f4445324e5473784b414977703457436e767a2f2f2f2f2f41513d3d227d; JSESSIONID=DE50AC8F279C14D51E88360142E23DEB; isg=BDw8S8hJco8-v0azaOpH8UvLDdruNeBf8HwIEha9SCcK4dxrPkWw77JTwQmZshi3; l=eBNF24eHLEgm-mcyBOfanurza77OSIRYYuPzaNbMiOCP9HCB5WcRW6VYvFY6C3GVh6xyR3-3_vV2BeYBqQAonxv92j-la_kmn; tfstk=cvbFBOtzSyUFCS87DeTzdsCMocfdwV5hZVRXxMF7r_bfbBfm5YdgMFAwNfkkx"
    }
    try:
        r = requests.get(url,headers=head,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR!"

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        return "ERROR!"

def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:32}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodslist(infoList)

main()