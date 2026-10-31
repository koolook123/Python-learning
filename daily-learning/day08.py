# 【今日目标】  
# 能把一段逻辑抽成函数，会用参数传值、用 return 拿结果。从今天开始，写代码前先问一句：这块能不能起个名字？

# 【知识点】7 条

# 1. def 名字(参数): 缩进体。没有 return 时返回 None，不是 0，不是空串。
# 2. return 一旦执行，函数立刻结束，它后面的代码是死代码。
# 3. 参数是「位置对应」的：f(a, b) 按顺序塞进去，与你起的参数名无关。
# 4. 函数内定义的变量出了函数就看不见（作用域，明天细讲）。
# 5. 返回值可以是多个：return min_v, max_v —— 本质是返回 tuple，调用处解包接受。
# 6. 函数名用动词：get_avg / count_words / is_valid。看到名字就该知道它干什么。
# 7. 一个函数只做一件事。超过 30 行就该考虑拆。

# 【今日题目】4 道｜A/B/C 必做

# A 基础 · 平均值（8 分钟）  
# 题目：写 get_avg(nums)，返回列表平均值；空列表返回 0.0。  
# 要求：自己判断空列表，不许让它抛 ZeroDivisionError。

# B 应用 · 词频函数（15 分钟）  
# 题目：写 count_words(text) 返回词频字典，再用它输出前 3 高频词。  
# 要求：函数只负责统计；排序和打印放在函数外面（职责分离）。

# C 变式 · 一次返回三个值（20 分钟）  
# 题目：写 stats(nums) 一次返回（最小值, 最大值, 平均值），调用处解包。  
# 要求：不许返回 list，不许用全局变量。

# D 拔高 · 消灭重复（选做，10 分钟）  
# 题目：把 D07 B 题里复制了 3 次的那段代码，改成 1 个函数调用 3 次。  
# 要求：数一下改前改后各多少行，把数字写下来。

# 【Git 10 分钟】  
# git diff 能看未提交的改动，红减绿增。  
# 任务：改一个文件 → 跑 git diff → 说出你改了哪几行 → 再提交。

# 【验收标准】

# 1. 三个函数都能跑，A 题空列表不报错。
# 2. 能说出「没写 return」和「写了 return None」的区别。
# 3. C 题那行解包代码能默写出来。


#A
def get_avg(_list):
    if _list==[]:
        return 0.0
    return sum(_list)/len(_list)

s=[1,2,3,4,5]
print(get_avg(s))


#B
def count_words(text):
    if text=="":
            return {}
    words=text.lower().split()

    clean=[]
    for i in words:
        i=i.strip("!?,.\"'")
        if i!="":
            clean.append(i)

    s={}
    for k in clean:
        s[k]=s.get(k,0)+1
    return s

text="The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs! Quick, quick!"
_dict=count_words(text)

top3=sorted(_dict.items(),key=lambda kv:(-kv[1],kv[0]))[:3]
for k,v in top3:
    print(k,v)


#C
def stats(nums):
     if not nums:
          return 0,0,0.0
     _min=min(nums)
     _max=max(nums)
     _avg=sum(nums)/len(nums)
     return _min,_max,_avg

nums = [88, 92, 75, 60, 100, 43, 67, 91]
__min,__max,__avg=stats(nums)
print(__min,__max,__avg)

#test git diff