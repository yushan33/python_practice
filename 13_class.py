# class 類別名稱:
#     定義封裝的變數
#     定義封裝的函式

# 定義類別
class IO :
  supportedSrcs = ["console", "file"]
  def read(src):
    if src not in IO.supportedSrcs:
      print("Not Supported")
    else:
      print("Read from ",src)
# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("Internet")
