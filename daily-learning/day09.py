# 【今日目标】  
# 搞清两件事：参数默认值什么时候算一次、变量在哪儿活得下去。这是 Python 最经典的两个面试题，也是真实 bug 的高发区。

# 【知识点】7 条

# 1. 默认值在**函数定义时**求值一次，不是每次调用。可变默认值（[] / {}）会被所有调用共享。
# 2. 正确写法：def f(x, lst=None): 然后在函数内 if lst is None: lst = []
# 3. 参数顺序：无默认值在前，有默认值在后，否则语法错。
# 4. \*args 把多余位置参数收成 tuple；\*\*kwargs 把多余关键字参数收成 dict。
# 5. LEGB 查找顺序：Local → Enclosing → Global → Built-in。
# 6. 函数内给全局变量赋值，必须写 global，否则等于新建一个同名局部变量（全局那份压根没变）——高频坑。
# 7. 函数内「读」全局变量不用声明，「写」全局变量必须声明。

# 【今日题目】4 道｜A/B/C 必做

# A 基础 · 复现经典 bug（10 分钟）  
# 题目：def add(item, lst=[]): lst.append(item); return lst。连调三次，打印结果。  
# 要求：解释为什么三次结果不是各自独立。

# B 应用 · 修好它（15 分钟）  
# 题目：把 A 题修好，两种写法各写一遍：None 哨兵 / 函数内 copy。  
# 要求：说明两种写法的差别，以及什么时候选哪个。

# C 变式 · 可变参数（20 分钟）  
# 题目：写 sum_all(\*nums) 接受任意个数字求和；再写 build_query(\*\*kwargs) 把关键字拼成 "a=1\&b=2"。  
# 要求：两个都写，不许 import。

# D 拔高 · 制造错误（选做，10 分钟）  
# 题目：写一段代码故意制造 UnboundLocalError：函数内给全局变量赋值但没加 global。  
# 要求：把报错原文抄下来，并标注报错指向哪一行。

# 【Git 10 分钟】  
# git restore 能撒销未暂存的改动，改坏了能一键退回。  
# 任务：故意改坏一个文件 → git diff 确认 → git restore 文件名 → 确认恢复原样。

# 【验收标准】

# 1. A 题能讲清「三次共用一个列表」的原因。
# 2. B 题两种写法都能跑且结果一致。
# 3. 能说出不加 global 会发生什么，而不是只背「要加 global」。


#A
def add(item, lst=[]): lst.append(item); return lst#bug


#B
#None:
def add(item,lst=None): 
    if lst is None:
        lst=[]
    lst.append(item)
    return lst

#.copy():
def add(item,lst=[]): 
    if lst==[]:
        lst=lst.copy()
    lst.append(item)
    return lst


#C
#top1:
def sum_all(*nums):
    return sum(nums)

#top2:
def build_query(**kwargs):
    str=""
    for k,v in kwargs.items():
        if str!="":
            str=str+"&"
        str=str+f"{k}={v}"
    return str