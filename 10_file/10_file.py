# 檔案操作流程
#     開啟檔案 >讀取或寫入 >關閉檔案

### 開啟檔案
# 檔案物件 = open(檔案路徑 , mode =開啟模式)

## 開啟模式
# 讀取模式 -r
# 寫入模式 -w
# 讀寫模式 -r+

### 讀取檔案
## 讀取全部文字
# 檔案物件.read()

## 一次讀取一行
# for 變數 in 檔案物件:
#     從檔案依序讀取每行文字到變數中

## 讀取json 格式
# import json
# 讀取到的資料 = json.load(檔案物件)

### 寫入檔案
## 寫入文字
# 檔案物件.write(字串)

## 寫入換行符號
# 檔案物件.write(字串+"\n")

## 寫入json格式
# import json
# json.dump(寫入的資料,檔案物件)

###  關閉檔案
# 檔案物件.close()

### Python 提供最佳實務的作法
# with open (檔案路徑, mode=檔案開啟模式) as 檔案物件 :
#     讀取或寫入檔案的程式
# 以上去塊會自動、安全的關閉檔案

#----- 練習 -----

## 檔案操作
# ---標準寫法---
file = open ("data.txt", 'w', encoding="utf-8")   #開啟檔案
file.write("Hello File\nSecond Line\n")    #寫檔案
file.write("測試中文\n安安你好給約嗎\n")
file.close()    #關閉

# ---最佳實務---
with open("data2.txt", mode = "w", encoding="utf-8") as file:
    file.write("5\n3\n1")

## 讀取檔案
# ---讀取整個檔案並顯示---
with open ("data.txt", mode = "r" ,encoding="utf-8") as file:
    data = file.read()
print(data)

# ---逐行讀取並將每行數字加減---
sum = 0
with open ("data2.txt", mode = "r" ) as file2:
    for line in file2:      #逐行讀取   
       sum += int(line)
print(sum)

## 使用json格式讀取、複寫檔案
import json
# 從檔案中讀取 json 資料，放到變數 data 中
with open ("config.json" , mode = "r") as file:
    data = json.load(file)
print(data) #data是一個字典資料
print("name :", data["name"])   
print("version :",data["version"])

data['name'] ="New Name"    #修改變數中的資料

# 把最新的資料複寫回檔案中
with open ("config.json" , mode = "w") as file:
    data = json.dump(data,file)