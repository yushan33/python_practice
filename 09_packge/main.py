# Package 套件
# 包含模組的資料夾，用來整理、分類模組的程式

### 專案檔案配置
# - 專案資料夾
#     - 主程式.py
#     - 封包資料夾
#         - __init__.py
#         - 模組一.py
#         - 模組二.py

### 載入封包
# import 封包名稱.模組名稱
# import 封包名稱.模組名稱 as 別名


##主程式
import geometry.point
d = geometry.point.distance(3,4)
print("距離:", d)

import geometry.line as line
s = line.slope(1,1,2,3)
print("斜率:", s)



# python 執行程式時會把執行時產生的一些資料放在 _pycache_ 資料夾，方便下次執行時更快速。
# 所以可以不用理會他，刪除也沒關係。
