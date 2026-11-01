#A
def get_avg(_list):
    if _list==[]:
        return 0.0
    return sum(_list)/len(_list)

if __name__=="__main__":
    st=[1,2,3,4,5]
    print(get_avg(st))


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

if __name__=="__main__":
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

if __name__=="__main__":
    nums = [88, 92, 75, 60, 100, 43, 67, 91]
    __min,__max,__avg=stats(nums)
    print(__min,__max,__avg)