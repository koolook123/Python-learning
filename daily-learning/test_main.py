from main import students,add_student

def test_add_normal():
    students.clear()
    ok=add_student("张三",90)
    assert ok is True
    assert len(students)==1
    assert students[0].name=="张三"

def test_duplicate_name():
    students.clear()
    add_student("张三",90)
    ok=add_student("张三",85)
    assert ok is False
    assert len(students)==1

def test_empty_name():
    students.clear()
    ok=add_student("",90)
    assert ok is False
    assert len(students)==0

if __name__=="__main__":
    test_add_normal()
    test_duplicate_name()
    test_empty_name()
    print("pass")