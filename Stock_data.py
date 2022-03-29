import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLtext(url):
    kv = {
        "Cookie":"prov=cn0791; city=0791; weather_city=jx_nc; vjuids=544204792.17fd083877f.0.8c68e5a1a71fd; vjlast=1648470755.1648470755.30; region_ip=182.100.25.246; user_saw_stock_map=sh600623%3A%u534E%u8C0A%u96C6%u56E2%3A1648470926341; userid=1648470926363_uw6uzu6379; region_ver=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
    }
    try:
        r = requests.get(url, headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "Error!"


def getStockList(lst, stockUrl):
    for i in range(1, 35):
        html = getHTMLtext(stockUrl+str(i))
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.find('table').children:
            if isinstance(tr, bs4.element.Tag):
                try:
                    lst.append(tr.find_all('td')[0].string)
                except:
                    continue
    return ""

def getStockInfo(lst, stockUrl, fpath):
    count = 0
    infoDict = {}
    lst = list(filter(lambda x: x != None, lst))
    for stock in lst:
        url = stockUrl + stock
        html = getHTMLtext(url)
        soup = BeautifulSoup(html, "html.parser")
        try:
            stockname = str(soup.find("h2", attrs={'class':'basic-stock-name'}).get_text())
            try:
                stockdata = str(soup.find("span", attrs={'class':'stock-price increase'}).get_text())
            except:
                stockdata = str(soup.find("span", attrs={'class': 'stock-price decrease'}).get_text())
            infoDict[stockname] = stockdata
            count += 1
            if count % 20 == 0:
                print('进度为：' + str(count) + '/'+str(len(lst)))
        except:
            count += 1
            print('有一个错误')
            continue
    with open(fpath, "w", encoding="utf-8") as f:
        for key in infoDict :
            f.write(key + ':' + infoDict[key] + "\n")
    return "ok"

def main():
    stock_list_url = "https://app.finance.ifeng.com/list/stock.php?t=ha&f=chg_pct&o=desc&p="
    stock_info_url = "https://www.laohu8.com/stock/"
    fpath = "./StockInfo.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, fpath)

main()