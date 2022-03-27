import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR!"

def fillUnivlist(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag) :
            tds = tr("td")
            name = tr.find("a", class_="name-cn").string
            ulist.append([tds[0].string.strip(), name, tds[4].string.strip()])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^15}\t{2:^10}"
    print(tplt.format("排名","学校","评分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/202111"
    html = getHTMLText(url)
    fillUnivlist(uinfo, html)
    printUnivList(uinfo, 30)

main()
