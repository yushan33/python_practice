#### 集合 ####
s1={3,4,5}

# in / not in 檢查元素是否在此集合中
print(3 in s1)  #True
print(10 in s1) #False
print(10 not in s1) #True

#集合的運算 &交集
s1 = {1,2,3,4}
s2 = {3,4,5}
s3 = s1 & s2    #交集:取兩集合中，相同的資料  #{3,4}
s3 = s1 | s2    #聯集:取兩集合中所有資料但不重複取 #{1,2,3,4,5}
s3 = s1 - s2    #差集:從s1中，減去和s2重疊的部分    #{1,2}
s3 = s1 ^ s2    #反交集:取兩個集合中，不重疊的部分  #{1,2,5}
print(s3)   

#set(字串) :將字串拆解成不重複元素的集合(因為無順序性，每次顯示會不一樣)
s= set("Hello")     #s ={'l', 'e', 'o', 'H'}
print(s)
print('H' in s)     #True
print("A" in s)     #False


#### 字典 ####

#字典:key-value配對
dic = {"apple": "蘋果","bug":"蟲子"}

#用鍵找值
print(dic['apple']) #蘋果

#修改值
dic['apple']="小蘋果"
print(dic['apple']) #小蘋果

#in / not in 檢查key是否在此集合中
print("apple" in dic)       #True
print("test" in dic)        #False
print("test" not in dic)    #True

#刪除字典中的鍵值對
print(dic)          #{'apple': '小蘋果', 'bug': '蟲子'}
del dic['apple']
print(dic)          #{'bug': '蟲子'}


#從列表中產生字典
#dic ={ x : x*2 for x in 列表}
list1 = [1,2,3]
dic = {x : x*2 for x in list1}
print(dic)