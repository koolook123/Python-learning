# 【今日目标】  
# 第 2 次复盘 + 第一次用类写代码。重点不是背语法，是理解「类和函数到底差在哪」。

# 【先复盘：4 问】

# 1. 这周（10.26-11.01）实际学几天、每天几分钟？
# 2. 函数 / 默认参数 / 模块 / 文件 / 异常 五个板块，哪个还写不利索？
# 3. 有没有因为「没写编码参数」或「裸 except」报过错？记下来。
# 4. 下周（项目周）只改一件事，改什么？

# 【知识点】6 条

# 1. 类 = 数据 + 操作这些数据的函数，打包在一起。函数是「做一件事」，类是「描述一个东西会做什么」。
# 2. class 名用大驼峰（Student），不是 student 也不是 student_class。
# 3. **init** 是构造时自动调用的方法，self 就是「这个对象自己」。
# 4. self 不是关键字，只是约定俗成的第一个参数名。写成 this 也能跑，但不要。
# 5. 实例属性 self.x 每个对象各一份；类属性写在 class 底下，所有对象共享——改一个影响全部。
# 6. 什么时候该用类：多个字段需要绑在一起，且要对它做多种操作时（如 Student 的姓名+成绩+平均分）。

# 【今日题目】3 道（复盘日减量）

# A 基础 · 第一个类（15 分钟）  
# 题目：写 Student 类，属性姓名、成绩（列表），方法 avg() 返回平均分。  
# 要求：创建 2 个学生，各打印平均分。

# B 应用 · 带校验的方法（20 分钟）  
# 题目：给 Student 加 add_score(score)，内部用 D12 的校验抛 ScoreError。  
# 要求：非法分数加不进去，且原数据不被污染。

# C 变式 · 班级类（20 分钟）  
# 题目：写 Clazz 类，内部用列表保存多个 Student；方法 class_avg() 返回全班平均分，best() 返回最高分学生姓名。  
# 要求：不许用全局变量。

# 【Git 10 分钟】  
# 任务：跑 git log --oneline 数本周 commit 条数，写进复盘。

# 【验收标准】

# 1. 复盘 4 问都有答案，第 1 问必须是数字。
# 2. 三个类都能实例化并调通。
# 3. 能说出「类属性和实例属性」的区别，各举一个会出错的场景。


#AB
class ScoreError(Exception):
    pass

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def add_score(self,score):
        if not(0<=score<=100):
            raise ScoreError(f"非法数字:{score}")
        self.scores.append(score)

a = Student("张三", [90, 85, 77])
b = Student("李四", [92, 68, 100])
print(a.name, a.avg())
print(b.name, b.avg())

#test:
s=Student("王五",[80])
s.add_score(95)
print(s.scores)

try:
    s.add_score(120)
except ScoreError as e:
    print("数字错误",e)


#C
class Clazz():
    def __init__(self):
        self.students=[]

    def add(self,student):
        self.students.append(student)

    def class_avg(self):
        total=0
        count=0
        for stu in self.students:
            total+=sum(stu.scores)
            count+=len(stu.scores)
        return total/count

    def best(self):
        top=self.students[0]
        for stu in self.students[1:]:
            if stu.avg()>top.avg():
                top=stu
        return top.name

c = Clazz()
c.add(Student("张三", [90, 85, 77]))
c.add(Student("李四", [92, 68, 100]))
c.add(Student("王五", [80, 95]))
print("全班平均分:", c.class_avg())
print("第一名:", c.best())