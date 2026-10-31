# """【今日 D03 · 10.22 周四】列表

# 【知识点】
# · 索引与负索引，切片 a[1:4] / a[::-1]
# · 增删改：append / insert / remove / pop / del
# · sort 原地改，sorted 返回新表

# 【今天的题】
# A 基础
# `nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]` 去重并保持原顺序，输出结果和长度。再用 `set` 写一遍，对比两次输出

# B 应用
# 同一个列表：输出去重后的最大值、最小值、平均值（2 位），以及最大值在原列表里的下标

# C 变式
# 找第二大的数（重复值算同一个）。全相同或不足 2 个元素时输出"没有第二大"。不许 sort 后取倒数第二个

# 【Git 10 分钟】
# `git status -s` 的三个标记：`??` 新文件没跟踪 · `A` 已暂存 · `M` 改过没暂存
# 存盘 `day03.py` → `git status -s` 看到 `??` → `git add day03.py` 变成 `A` → commit 后整行消失

# 【验收】
# 不看答案写出去重 + 找第二大

# ————————————
# 90 主任务 + 30 中断 + 30 练习（20 做题 + 10 Git），时段自定，中间要断开
# 三题都不许先看答案，卡 20 分钟先跳，把卡点记下来
# 收尾：git add . → git commit -m "add: 第3天 列表" → git push"""

#A
nums=[3,1,4,1,5,9,2,6,5,3,5]

result=[]
for i in nums:
    if i not in result:
        result.append(i)
print(result,len(result))

result_set=set(nums)
print(result_set,len(result_set))


#B
_max=max(result)
_min=min(result)
_avg=sum(result)/len(result)
_idx=nums.index(_max)

print(f"最大值{_max},最小值{_min},平均值{_avg:.2f},下标{_idx}")


#C
#不用.sort
_nums=nums.copy()
if _nums==[]:
    print("没有第二大")
else:
    nums_max=max(_nums)

    while nums_max in _nums:
        _nums.remove(nums_max)

    if _nums!=[]:
        nums_max02=max(_nums)
        print(f"第二大为{nums_max02}")
    else:
        print("没有第二大")