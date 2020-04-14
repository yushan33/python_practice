import urllib.request as req
import bs4

def getData(url):
    request =req.Request(
        url , 
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "cookie":"over18=1"
        }
    )

    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    # print(data)

    
    root = bs4.BeautifulSoup(data , "html.parser")
    titles = root.find_all("div",class_="title")
    with open ("data.txt", mode = "a" ,encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                print(title.a.string)
                file.write(title.a.string+"\n")

    # 抓取上一頁的連結 
    nextLink = root.find("a",string="‹ 上頁")   #找到內文是 ‹ 上頁的a 標籤
    return nextLink["href"]

#主程序: 抓取一個頁面的標題
pageUrl =  "https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(10):
    pageUrl = "https://www.ptt.cc"+getData(pageUrl)
print(pageUrl)

