# 【今日目标】  
# 第一次把代码拆成多个文件并跑通；同时把调试方式从「到处 print」升级到「会断点」。拆完文件后调用链变长，print 就不够用了。

# 【知识点】7 条

# 1. import 模块 / from 模块 import 名字 / import 模块 as 别名。优先第一种，来源清楚。
# 2. 一个 .py 文件就是一个模块，文件名就是模块名（不许中文、不许数字开头）。
# 3. if **name** == "**main**": 的意义——直接运行时为 True，被 import 时为 False。测试代码写在这里。
# 4. 标准库先用熟这几个：math / random / datetime / pathlib。
# 5. 模块搜索路径：当前目录 → 标准库 → 第三方。自己写的文件要跟主文件同目录。
# 6. **调试升级**：用 breakpoint() 或 IDE 行号旁点红点，能看变量、单步走、看调用栈。print 只适合临时看一个值。
# 7. 循环 import 会报错（A 引 B、B 引 A），改结构而不是硬绕。

# 【今日题目】4 道｜A/B/C 必做

# A 基础 · 拆文件（10 分钟）  
# 题目：把 D08 的三个函数拆到 mytool.py，主文件用 from mytool import ... 调用。  
# 要求：mytool.py 里的测试代码放进 **main** 块。

# B 应用 · 随机与计时（15 分钟）  
# 题目：用 random 模拟掷骰子 1000 次，输出每个点数出现次数；用 datetime 或 time.perf_counter() 打印运行耗时。  
# 要求：统计部分用 dict 计数惯用法，不许逐个数。

# C 变式 · 用断点找 bug（20 分钟）  
# 题目：下面这段去重代码有坑（一边遍历一边删元素）：  
# def dedup(lst):  
# for x in lst:  
# if x in lst[:lst.index(x)]: lst.remove(x)  
# return lst  
# 要求：把断点设在哪一行、单步过程中看到了什么变量值，写下来。不许用 print 找。

# D 拔高 · pathlib 地基（选做，10 分钟）  
# 题目：用 pathlib.Path.cwd() 打印当前工作目录，列出该目录下所有 .py 文件名。  
# 要求：这是明天文件操作的预备，先熟个脸。

# 【Git 10 分钟】  
# 任务：跑一遍程序（会生成 **pycache**/）→ git status 看它有没有被忽略 → 如果没被忽略，说明 .gitignore 失效，找原因。

# 【验收标准】

# 1. 拆成两个文件后程序照常运行。
# 2. 能解释 **name** == "**main**" 到底有什么用。
# 3. C 题能说清断点设在哪一行、看到了什么。


#A
from mytool import get_avg
print(get_avg([1,2,3,4,5]))

from mytool import count_words
text="The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs! Quick, quick!"
_dict=count_words(text)

top3=sorted(_dict.items(),key=lambda kv:(-kv[1],kv[0]))[:3]
for k,v in top3:
    print(k,v)

from mytool import stats
nums = [88, 92, 75, 60, 100, 43, 67, 91]
__min,__max,__avg=stats(nums)
print(__min,__max,__avg)


#B
import random,time

start=time.perf_counter()

total=[]
for count in range(1000):
    total.append(random.randint(1,6))
total.sort()

result={}
for k in total:
    result[k]=result.get(k,0)+1

for k,v in result.items():
    print(f"{k}:{v}")

finish=time.perf_counter()
print(finish-start)


#C
#题目：下面这段去重代码有坑（一边遍历一边删元素）：  
# def dedup(lst):  
#     for x in lst:  
#         if x in lst[:lst.index(x)]: 
#             lst.remove(x)  
#     return lst  

# lst=[1,2,2,3,3,3]
# print(dedup(lst))