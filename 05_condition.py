# 【 if 結構 】
# 條件不需要() ，迴圈不需要{}

# if 條件:
#   true->執行命令 
# elif 條件二:
#   true->執行命令
# else:
#   其他->其他的命令

# and 且
# or 或
# not 非

# 不支援switch

###### 數字大小 ######
x = input("input number:")  #輸入的型態為字串
x = int(x)  #轉換成整數型態
if x  > 200:
    print("Greater than 200")
elif x < 200 and x > 100:
    print("Greater than 100 and less than 200")
else:
    print("Less than 100")


####### 四則運算 ######
n1 =int(input("Please input number1 "))
n2 =int(input("Please input number2 "))
operation =input("input operation: +,-,*,/")

if operation == "+":
    print(n1+n2)
elif operation =="-":
    print(n1-n2)
elif operation =="*":
    print(n1*n2)
elif operation =="/":
    print(n1/n2)
else:
    print("無法支援此運算")

