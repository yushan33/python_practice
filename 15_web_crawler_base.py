# --- 基本網路爬蟲 ---
# 抓取html的資料，要看起來像是人去點選資料，否則會被拒絕
#       網頁->開發者資訊(F12)->Network->重新整理畫面後 ->看網頁(html檔)->Headers->Request Headers ->就會有user-agent資訊
# 格式為html 故要先用pip 安裝 BeautifulSoup 套件
#       終端機輸入 :pip install beautifulSoup4

### 抓取PTT抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個Request物件，附加上Request Headers的資訊 #user-agent:告訴網站使用哪個作業系統與哪種瀏覽器
request =req.Request(url , headers ={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
})
with req.urlopen(request) as response :
    page = response.read().decode("utf-8")
#print(page)


### 解析原始碼，取得每篇文章的標題
# 安裝beautifulSoup4

# 載入beautifulSoup4套件
import bs4 

root = bs4.BeautifulSoup(page , "html.parser")  #告訴beautifulSoup4資料端與資料種類(為html)，讓Beautifulsoup 協助我們解析HTML格式文件
print("網頁的標題 : ",root.title.string)   #抓到網頁的title

title = root.find("div", class_="title")   #尋找 第一個class="title"的div標籤
print("第一個標題 :",title.a.string)  #找到class="title"的div標籤中，被<a></a>包含的字串

titles = root.find_all("div", class_="title")   #尋找所有 class="title"的div標籤
for t in titles:
    if t.a != None: # 如果標題包含 a標籤(沒有被刪除)，才印出來
        print(t.a.string)