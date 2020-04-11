#### 定義函式
# def 函式名稱(參數):
#     函式內部程式碼
#     return 資料(不回傳資料可不寫return 或只寫return)

def sayHello():
    print("Hello")

def saymsg(msg):
    print(msg)

def add(n1,n2):
    return n1+n2

def add2(n1,n2):
    r = n1+n2
    return "Funtion Add()"

def add3(n1,n2):
    r = n1+n2
    return  #return None

#### 呼叫函式
sayHello()
saymsg("Hello World")
saymsg("Hello Python")
print(add(1,2))
print(add(3,4))
print(add2(3,4))
print(add3(3,4))

def sumAll(n1,n2):
    sum =0
    for i in range(n1,n2+1):
        sum += i
    return sum

print(sumAll(1,10)) 


#### 參數預設資料
# def 函式名稱(參數名稱 =  預設資料):
#     函式內部的程式碼

def saymsg2(msg = "Hello"):
    print(msg)

saymsg2()
saymsg2("Hello World")

#### 不管函式順序，以參數名稱對應資料
# def 函式名稱(參數1,參數2):
#     函式內部程式碼

## 呼叫函式，以參數名稱對應資料
# 函式名稱(參數2=參數值,參數1=參數值)

def divide(n1,n2):
    print (n1/n2)

divide(2,4)
divide(n2= 4, n1=2)


#### 無限/不定 參數資料
# def 函式名稱(*無限參數):
#     #無限參數以Tuple資料形態處理
#     函式內部的程式碼

def say(*msgs):
    for msg in msgs:
        print(msg)

def avg(*nums):
    sum=0
    for i in nums:
        sum+=i
    print("平均數為: ",sum/len(nums))

# # 呼叫函式，可傳入無線數量的參數
# 函式名稱(data1,data2,data3...)

say("Hello", "today" ,"Monday") 
avg(1,2,3,4,5)
avg(10,11,12)
avg(1)
avg(3,4)
avg(3,5,10)
avg(1, 4,-1,-8)


