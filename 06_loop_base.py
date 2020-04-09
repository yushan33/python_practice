##while用法
n = 1
while n < 5:
    print("變數n 值為",n)
    n+=1

# 1+2+3...+10
n2=0
all=0
while n2<10:
    print("n value is :",n2)
    n2+=1
    all+=n2

print("all value is :",all)


##for in 用法
####數值陣列
for i in [4,1,2]:
    print("i's value is :", i)

####字串陣列
for s in "HelloWorld":
    print ("s value is :", s)



### range() :製造連續數字的列表
# for i in range(3):
# 等同於
# for i in [0,1,2]:

for i in range(3):
    print("i value is :", i)

# range(起始值,結束值)  :製造連續數字的列表，不包含結束值
# for i in range(3,6):
# 等同於
# for i in [3,4,5]:
for i1 in range(3,6):
    print("i1 value is :", i1)
    
# 累加1~10
sum = 0
for i2 in range(11):
    sum +=i2
print("sum value is :" ,sum)