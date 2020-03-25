####  數字運算  ####

#小數除法
x=3/6
print(x)

#整數除法
x=3//6
print(x)

#次方運算 x的y次方 =>x**y
x=2**3
print(x)

#取餘數
print(8%3)

#### 字串運算####

#跳脫字元 \
s='Amy\'s Day'
print(s)

#字串串接
s= "Hello" + "World"
print(s)

#字串換行 \n """字串"""
s ="Hello \n World1"
print(s)

s = """Hello
World2
"""
print(s)

#字串重複 :字串*重複次數
s = "Hello" *3 +"World"
print(s)

#字串索引，從0開始算
#字串(開頭:結尾) 取得字串包含開頭不包含結尾字串
#字串(開頭:)   取得字串開頭至最後
#字串(:結尾)   取得字串結尾前所有字串(不包含結尾)
s = "Hello"
print(s[1])     #e
print(s[1:4])   #ell
print(s[1:])    #ello
print(s[:3])    #Hel
