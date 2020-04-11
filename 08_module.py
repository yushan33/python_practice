### 載入模組
# import 模組名稱(不須加py)
# import 模組名稱 as 模組別名

### 使用模組
# 模組名稱(或別名).函式名稱(參數資料)
# 模組名稱(或別名).變數名稱

### 內建模組
# sys : 取得系統相關資訊
# import sys

# print(sys.platform)     #印出作業系統
# print(sys.maxsize)      #印出整數型態的最大值
# print(sys.path)         #印出搜尋模組的路徑

# import sys as s
# print(s.platform)     #印出作業系統
# print(s.maxsize)      #印出整數型態的最大值
# print(s.path)         #印出搜尋模組的路徑

### 自訂模組(在這個檔案放了一個叫做geometry.py)
# import geometry
# result =  geometry.distance(1,1,5,5)
# print(result)
# result = geometry.slope(1,2,5,6)
# print(result)

### 調整搜尋模組的路徑
import sys
sys.path.append("modules")  #在模組的搜尋路徑列表中【新增路徑】，請python多一個搜尋檔案的路徑
print(sys.path)
import geometry
result =  geometry.distance(1,1,5,5)
print(result)
