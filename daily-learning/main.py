class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

students=[]

def add_student(name,score):
    if not name:
        return False
    for s in students:
        if s.name==name:
            return False
    students.append(Student(name,score))
    return True

def list_students():
    return students

def main():
    while True:
        print("1-add")
        print("2-all")
        print("0-exit")

        choice=input("选择：")
        if choice=="0":
            break
        elif choice=="1":
            name=input("名字：")
            try:
                score=input("分数：")
            except ValueError:
                print("成绩必须是数字")
                continue
            if add_student(name,score):
                print("已添加")
            else:
                print("添加失败（姓名空或重名）")
        elif choice=="2":
            for s in list_students():
                    print(f"{s.name,s.score}")
        else:
            print("输错了")

if __name__=="__main__":
    main()