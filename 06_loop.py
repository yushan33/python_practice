# ##while用法
# n = 1
# while n < 5:
#     print("變數n 值為",n)
#     n+=1

# # 1+2+3...+10
# n2=0
# all=0
# while n2<10:
#     print("n value is :",n2)
#     n2+=1
#     all+=n2

# print("all value is :",all)


# ## for in 用法
# # 數值陣列
# for i in [4,1,2]:
#     print("i's value is :", i)

# # 字串陣列
# for s in "HelloWorld":
#     print ("s value is :", s)



# ### range() :製造連續數字的列表
# # for i in range(3):
# # 等同於
# # for i in [0,1,2]:

# for i in range(3):
#     print("i value is :", i)

# # range(起始值,結束值)  :製造連續數字的列表，不包含結束值
# # for i in range(3,6):
# # 等同於
# # for i in [3,4,5]:
# for i1 in range(3,6):
#     print("i1 value is :", i1)
    
# # 累加1~10
# sum = 0
# for i2 in range(11):
#     sum +=i2
# print("sum value is :" ,sum)


##  break、continue
# break :跳出迴圈
# continue :迴圈強制執行下一次

# n = 1
# while n < 5 :
#     if n ==3:
#         break
#     print(n)
#     n+=1
# print(n)    #n = 3

# n = 0
# for x in [0,1,2,3]:
#     if x % 2 ==0:
#         continue    #x = 0與2時，n不加1
#     n+=1
# print(n)    #n =2



# ### else :迴圈結束前，最後一次需要執行的動作 
# n=1
# while n<5:
#     n+=1
# else:
#     print(n)    #n=5

# for s in "Hello":
#     print("逐一取得字串 s :", s)
# else:
#     print("最後一字 :", s)  #最後一字 : o

# sum = 0
# for n in range(11): 
#     sum+=n
# else:
#     print ("1+...+10 = ",sum)   #1+...+10 =  55


### 輸入數字，找出整數平方根
x = int(input("輸入數字，找整數平方根"))
for i in range(x+1):
    if i*i==x:
        print("整數平方根為",i )
        break   #用break強制結束迴圈時，不會執行else區塊
else:
    print("此數沒有整數平方根")
 
        
