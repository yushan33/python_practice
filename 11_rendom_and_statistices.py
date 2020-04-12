
### ---隨機模組 ---- ###
import random
data = [1,5,6,10,20]

# 隨機選取
choice = random.choice(data)
print("Choice :" , choice )

# 隨機選取多筆資料
choice2 = random.sample(data, 3)    #隨機選取三筆資料
print("Choice 3 :", choice2)

# 隨機「就地」調換順序(洗牌)
# data = [1,5,6,10,20]
random.shuffle(data)
print(data)

# 隨機取的亂數，預設函數為0~1之間
r = random.random() #取0~1之間的數，包含0不包含1
print("隨機取0~1之間的數 :",r)

r = random.uniform(0.0,1.0) #取0~1之間的數，包含0與1
r2 = random.uniform(60,100)
print("隨機取0~1之間的數 :",r)
print("隨機取60~100之間的數 :",r2)

# 取得常態分配的亂數
# 平均數 100，標準差10 ，得到的資料多數在90~100之間
r3 = random.normalvariate(100,10)
print("常態分配的亂數 :",r3)

# 平均數 0 ，標準差 5 ，得到的資料多數在-5~5之間
r3 = random.normalvariate(0 ,5)
print("常態分配的亂數 :",r3)


### ---統計模組 ---- ###
import statistics as stat
# 取平均數
m = stat.mean(data)
print("平均數為: ", m)

#取中位數
mid = stat.median(data)
print("中位數 :", mid)

#取標準差
dev = stat.stdev(data)
print("標準差 :", dev)
