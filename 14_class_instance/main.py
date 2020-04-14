### ---類別初始化---
'''
class 類別名稱:
    #定義初始化函式(固定名稱)
    def __init__(self):
        透過操作self來定義實體屬性

#建立實體物件，放入變數obj中
obj = 類別名稱()#呼叫初始化函式
'''

class Point:
    def __init__(self):
        self.x = 3
        self.y = 4

# 可放入變數
class Point2:
    def __init__(self, a , b ):
        self.x = a
        self.y = b
    def show (self):
        print("座標為 :", self.x ,self.y )
    def distance(self , targetX , targetY):
        return ((targetX-self.x)**2+(targetY-self.y)**2)**0.5

p =Point()
p2 =Point2(3,4)
print("呼叫p.x : ", p.x)
print("呼叫p2.x+p2.y :",p2.x + p2.y)
p2.show()
print("與原點座標距離為 :", p2.distance(0,0))

class FullName:
    def __init__(self , first ,last):
        self.firstName = first
        self.lastName =last

name = FullName("Tanya" ,"Shan") 
print(name.firstName , name.lastName)

# ---實體方法---
# 封裝在實體物件中的函式
'''
class 類別名稱:
    #定義初始化函式
    def __init__(self):
        定義實體屬性
    
    #定義實體方法/函式
    def 方法名稱(self ,更多自訂參數):
        方法主體，透過self操作實體物件

#建立實體物件，放入變數obj
obj = 類別名稱()

#呼叫實體方法:實體物件.實體方法名稱(參數資料)
obj.物件方法(參數資料)

'''
# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    def __init__(self ,name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name , mode ="r", encoding="UTF-8")
    def read(self):
        return self.file.read()

# 讀取第一個檔案    
file1 = File("data.txt")
file1.open()
data = file1.read()
print(data)

# 讀取第二個檔案
file2 = File("data2.txt")
file2.open()
data2 = file2.read()
print(data2)