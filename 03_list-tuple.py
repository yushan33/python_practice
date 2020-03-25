#### 有序變動列表 List []  ####
grades =[12,60,15,70,90]
print(grades)  #[12, 60, 15, 70, 90]
print(grades[0])    #12
print(grades[3])    #70

grades[0] = 66
print(grades)

#取出指定位置區間
print(grades[1:4])  #[60,15,70]

#刪除特定區間
grades[1:4]=[]
print(grades)       #[66,90]

#尾數加上新的數值
grades =[12,60,15,70,90]
grades +=[13,39]
print(grades)   #[12, 60, 15, 70, 90, 13, 39]

#取的列表長度 len(List)
print(len(grades))

#巢狀迴圈
data = [ [1,2,3],[10,11,12] ]
print(data[0][2])   #3
print(data[1][1])   #11

data[0][0:2]=[5,5,5]  #將0,1位置改成5,5,5
print(data)  #[ [5,5,5,3],[10,11,12] ] 



#### 有序不可動列表 Tuple () #####
data = (3,4,5,6)
print(data[1])
print(data[0:2])
# data[0]=5 #錯誤:Tuple的資料不可變動
