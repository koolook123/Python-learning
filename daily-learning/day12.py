# 【今日目标】  
# 让程序遇到坏输入不崩，并且**不掩盖真实错误**。今天一条硬禁令：不许写裸 except，不许写 except: pass。

# 【知识点】8 条

# 1. try / except / else / finally 四段的时机：except 出异常时执行，else 没异常时执行，finally 无论如何都执行。
# 2. 捕获要具体：except FileNotFoundError 而不是 except:。裸 except 会把 Ctrl+C、拼写错误全吞掉。
# 3. **绝对禁止**：except: pass。它让 bug 消失，但让问题留下。
# 4. except Exception as e: 然后用 f"...{e}" 打印或记日志。
# 5. raise 主动抛异常。raise ValueError("分数不能为负")——带消息才看得懂。
# 6. 自定义异常：class ScoreError(Exception): pass，比抛一艾字符串清楚。
# 7. EAFP vs LBYL：Python 偏爱「先做，出错再处理」（try），而不是「先检查再做」（if exists）。
# 8. finally 用于收尾：关文件、关连接、恢复状态。

# 【今日题目】4 道｜A/B/C 必做

# A 基础 · 输入不崩（10 分钟）  
# 题目：把「输入分数并转 int」写成循环，非数字就提示重输，直到输入合法。  
# 要求：用 try/except ValueError，不许用 isdigit() 预先判断。

# B 应用 · 分开处理（15 分钟）  
# 题目：写 safe_read(path) 读文件；文件不存在时返回 None 并打印提示，其他异常原样抛出。  
# 要求：必须把 FileNotFoundError 和其他 Exception 分开写两个 except。

# C 变式 · 自定义异常（20 分钟）  
# 题目：写成绩校验函数，分数必须 0-100，否则抛 ValueError("分数必须在 0-100 之间，收到：xxx")；再写自定义异常 ScoreError 并演示捕获。  
# 要求：错误消息里必须带实际收到的值。

# D 拔高 · 清理旧习（选做，10 分钟）  
# 题目：找一段你自己以前写的 try/except，检查有没有 except: pass 或裸 except，改掉。  
# 要求：写一句「原来它会吞掉什么」。

# 【Git 10 分钟】  
# commit 前自查。  
# 任务：git status 看有没有不该提交的文件 → git diff 检查有没有留下 print 调试语句、有没有写死的路径和密码 → 再提交。

# 【验收标准】

# 1. A 题输入 abc 不崩，能重输。
# 2. B 题能把「文件不存在」和「其他错误」分开处理。
# 3. 全文搜一遍自己的代码，确认没有 except: pass。


#A
while True:
    try:
        num=int(input("请输入数字："))
        break
    except ValueError():
        print("重输")


#B
def safe_read(path):
    try:
        with open(path,encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError():
        print("文件不存在")
        return None

    except Exception():
        print(f"{Exception}")
        raise


#C
def score_check(score):
    try:
        if 0>score>100:
            return score
    except ValueError():
        raise ValueError(f"分数必须在 0-100 之间，收到：{score}")
    except Exception():
        print("ScoreError(其他错误)")