# 網路連線
# import urllib.request as request
# src = "https://www.ntu.edu.tw"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")  #取得台灣大學網站的原始碼，若不加.decode("utf-8")，會看不懂原始碼的中文字
# print(data)


# 串接、擷取公開資料
import urllib.request as request
import json 

src = "https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-001556-002"       #縣（市）、鄉（鎮、市）與外國地方政府締盟情形彙整表

with request.urlopen(src) as response:
    data = json.load(response)  #利用JSON模組處理json資料格式

citylist = data["result"]["records"]

with open("data.txt",encoding="utf-8", mode="w") as file:
    for city in citylist:
        file.write(city["County_City_Town"] + ":" + city["TheAllie"] +"\n")







