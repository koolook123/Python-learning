# 【今日目标】  
# 会用字典做计数和查表，会用集合做去重与交并差。遇到「统计频次」「是否出现过」能立刻想到 dict / set，而不是写双层 for 循环。

# 【知识点】8 条，每条都要能口头讲清

# 1. 取值的三种写法：d[k] 键不存在直接 KeyError；d.get(k) 返回 None；d.get(k, 0) 返回你给的默认值。
# 2. 计数惯用法：d[k] = d.get(k, 0) + 1。这是后面所有统计题的地基，必须闭眼能写。
# 3. 遍历：for k in d 拿键；d.values() 拿值；d.items() 拿 (键, 值)。遍历过程中不要增删键，否则 RuntimeError。
# 4. 键必须可哈希：int / str / tuple 可以，list / dict 不行。
# 5. set 三特性：元素唯一、无序、查找 O(1)（list 是 O(n)）。
# 6. 空集合只能写 set()。写 {} 得到的是空字典——高频坑。
# 7. 集合运算：& 交、| 并、- 差、^ 对称差。
# 8. 按值排序：sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))。负号实现降序，第二个键处理并列。

# 【今日题目】4 道｜A/B/C 必做，D 选做

# A 基础 · 字符统计（8 分钟）  
# 题目：统计 "hello world" 里每个字符出现的次数，不统计空格，输出字典。  
# 要求：必须用 d.get(k, 0) + 1 的写法，不许用 collections.Counter。

# B 应用 · 词频前 2（15 分钟）  
# 题目：words = ["a","b","a","c","b","a"]，输出出现次数最多的前 2 个词及次数，次数相同按字母序。  
# 要求：一次 sorted 完成双键排序，不许分两趟。

# C 变式 · 字典合并（20 分钟）  
# 题目：成绩1 = {"张三":80,"李四":90}，成绩2 = {"张三":70,"王五":85}。合并两份，同名成绩相加，输出结果并按成绩降序打印。  
# 要求：不许 import 任何模块；成绩相同按姓名序。

# D 拔高 · 集合运算（选做，10 分钟）  
# 题目：A = ["张三","李四","王五","张三"]，B = ["王五","赵六","张三"]。  
# 要求：输出 (1) A 去重后的名单；(2) 两班都有的；(3) 只在 A 的。再用一句话回答：为什么 list 求交集比 set 慢。

# 【Git 10 分钟】  
# .gitignore 让 Git 彻底看不见某些文件，写进去就不算未跟踪。  
# 任务：仓库根目录建 .gitignore，写四行 **pycache**/ 、*.pyc 、.venv/ 、*.csv → 跑 git status 确认 **pycache** 不再出现 → 把 .gitignore 本身也提交。  
# 注意：.gitignore 自己必须提交，否则别人 clone 下来规则就丢了。

# 【验收标准】三条全过才算完成

# 1. 不看答案写出字符统计，并逐行解释每一行在干什么。
# 2. 能说出 d[k]、d.get(k)、d.get(k, 0) 三者的区别，各举一个使用场景。
# 3. 能解释为什么空集合要写 set() 而不是 {}。


#A
s="hello world"
count={}

for a in s:
    if a==" ":
        continue
    count[a]=count.get(a,0)+1

print(count)


#B
words=["a","b","a","c","b","a"]
count={}

for a in words:
    count[a]=count.get(a,0)+1

top2=sorted(count.items(),key=lambda _tuple:(-_tuple[1],_tuple[0]))[:2]
print(top2)


#C
re01={"张三":80,"李四":90}
re02={"张三":70,"王五":85}

sum={}
for d in (re01,re02):
    for name,result in d.items():
        sum[name]=sum.get(name,0)+result
print(sum)

sum=sorted(sum.items(),key=lambda kv:(-kv[1],kv[0]))
for name,result in sum:
    print(name,result)


#D
A = ["张三","李四","王五","张三"]
B = ["王五","赵六","张三"]

set_A=set(A)
set_B=set(B)

print(sorted(set_A))
print(set_A&set_B)
print(set_A-set_B)