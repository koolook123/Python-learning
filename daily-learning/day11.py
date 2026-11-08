# 【今日目标】  
# 能读写文本文件和 CSV，用 with 保证文件被关；知道编码问题为什么会让中文变乱码。

# 【知识点】8 条

# 1. with open(...) as f: —— 离开代码块自动关闭，不用手动 close()。
# 2. 三个模式：r 读、w 覆盖写（**文件已存在会直接被清空**）、a 追加。
# 3. 读法：f.read() 全读成一个大字符串；f.readlines() 读成列表（每行带 \n）；for line in f 逐行读（大文件用这个）。
# 4. 写法：f.write() 不自动加换行，要自己写 \n。
# 5. 编码：读中文一律写 encoding="utf-8"。Windows 默认 GBK，跨平台必踩。
# 6. CSV 用 csv 模块：csv.reader / csv.writer；读出来全是字符串，数字要自己转。
# 7. pathlib 比 os.path 好用：Path("data") / "a.txt" 拼路径，.exists() / .suffix / .stem。
# 8. 文件不存在会 FileNotFoundError——先判断 .exists()，或用 try（明天讲）。

# 【今日题目】4 道｜A/B/C 必做

# A 基础 · 写文件（10 分钟）  
# 题目：把 D08 的成绩统计结果写进 scores.txt，一行一个「姓名,分数」。  
# 要求：用 with + encoding="utf-8"。

# B 应用 · 读回文件（15 分钟）  
# 题目：读回 scores.txt，算平均分并输出。  
# 要求：用 for line in f 逐行读，不用 readlines；每行 strip() 后 split(",")。

# C 变式 · 转 CSV（20 分钟）  
# 题目：把 scores.txt 转成带表头的 CSV，再读回来按分数降序打印。  
# 要求：用 csv 模块，不许手工拼逗号。

# D 拔高 · 递归扫目录（选做，10 分钟）  
# 题目：写一个函数，递归列出指定目录下所有 .py 文件的路径和大小（字节）。  
# 要求：用 pathlib.Path.rglob("*.py")。

# 【Git 10 分钟】  
# 数据文件不该进仓库。  
# 任务：把 \*.txt 和 \*.csv 加进 .gitignore → 确认 git status 干净 → 提交 .gitignore 的这次改动。

# 【验收标准】

# 1. 文件写出再读回，中文不乱码。
# 2. 能说出 w 模式的最大风险是什么。
# 3. D 题能在自己项目目录跑出真实的文件列表。


#A
scores = [
    ("张三", 90),
    ("李四", 85),
    ("王五", 77),
    ("赵六", 92),
    ("钱七", 68),
    ("孙八", 100),
]

with open("scores-11.txt","w",encoding="utf-8") as f:
    for name,score in scores:
        f.write(f"{name},{score}\n")


#B
total=0
count=0

with open("scores-11.txt",encoding="utf-8") as f:
    for line in f:
        name,score=line.strip().split(",")
        total+=int(score)
        count+=1
    print(total/count)


#C
import csv

rows=[]

with open("scores-11.txt",encoding="utf-8") as f:
    for line in f:
        name,score=line.strip().split(",")
        rows.append([name,int(score)])

with open("scores-11.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["name","socre"])
    w.writerows(rows)

with open("scores-11.csv",newline="",encoding="utf-8") as f:
    data=list(csv.reader(f))

body=data[1:]
body.sort(key=lambda r: int(r[1]),reverse=True)

for name, score in body:
    print(f"{name}  {score}")