# 【今日目标】  
# 用 4 道综合题检验第 1 周 5 个板块（变量类型 / 条件循环 / 列表 / 字典集合 / 字符串方法），并完成第 1 次正式复盘。

# 【先复盘：4 问，不许写感想】

# 1. 这 7 天实际学了几天、每天平均多少分钟？（必须给数字）
# 2. 哪道题卡超过 20 分钟？卡在哪一行？
# 3. 5 个板块里，哪个现在让你重写还是写不出来？
# 4. 下周只改一件事，改什么？

# 【知识点回顾（20 分钟，只看不抄）】  
# · 变量与类型：int / float / str 互转，input() 拿到的一定是字符串  
# · 条件与循环：for 适合已知次数，while 适合未知次数；break / continue  
# · 列表：append / 索引 / 切片，sort 与 sorted 的区别  
# · 字典集合：get 计数、set 去重与交并差  
# · 字符串：strip / split / join / f-string 格式化

# 【今日题目】4 道，全部综合，不再单考一个知识点

# A 综合 · 成绩统计（15 分钟）  
# 用 input 循环输入若干成绩，输入空行结束。输出：最高分、最低分、平均分（两位小数）、及格率（60 分及以上占比，百分数两位小数）。  
# 要求：空输入要有提示，不许崩溃。

# B 综合 · 文本词频（20 分钟）  
# 给一段英文文本，统计每个单词出现次数，输出前 3 高频词及次数。  
# 要求：先 split() 清洗，再去标点（提示 str.strip(",.!?")），最后排序。

# C 变式 · 两班名单（20 分钟）  
# 两个班名单列表，求：两班都有的人、只在 A 班的人、总共有多少人（去重后）。  
# 要求：用 set 运算，一行一个运算，不要写 for 循环硬算。

# D 拔高 · 串成脚本（选做，10 分钟）  
# 用 5 行以内代码，把本周学过的 5 个知识点各写一个最小可运行示例，串成一个脚本。

# 【Git 10 分钟】  
# 任务：跑 git log --graph --oneline -10，数出本周 commit 条数，写进复盘里。commit 太少就说明这周有几天断了。

# 【验收标准】

# 1. 4 问复盘每问都有答案，第 1 问必须是数字。
# 2. A/B/C 三题能跑通，输入异常不崩。
# 3. 复盘记录发给 MOSS，存进资产 02-复盘/。


#A
s=0
num=[]
while True:
    s=input("请输入成绩（直接回车结束）: ")
    if s=="":
        print("输入结束")
        break
    if not s.isdigit():
        print("不是有效数字，请重新输入")
        continue
    num.append(int(s))

if len(num)==0:
    print("没有输入任何成绩")
else:
    _max=max(num)
    _min=min(num)
    _avg=sum(num)/len(num)

    _pass=[]
    for i in num:
        if i>=60:
            _pass.append(i)
    _passrate=len(_pass)/len(num)

    print(_max)
    print(_min)
    print(f"{_avg:.2f}")
    print(f"{_passrate*100:.2f}%")


#B
s=input()
s=s.lower()
s=s.split()

clean=[]
for i in s:
    i=i.strip("!?,.\"'")
    if i!="":
        clean.append(i)

count={}
for i in clean:
    count[i]=count.get(i,0)+1

top3=sorted(count.items(),key=lambda kv:(-kv[1],kv[0]))[:3]

for k,v in top3:
    print(k,v)


#C
A=["std01","std02","std03"]
B=["std03","std04","std05"]

_both=set(A)&set(B)
_justA=set(A)-set(B)
_all=set(A)|set(B)

print(_both)
print(_justA)
print(len(_all))