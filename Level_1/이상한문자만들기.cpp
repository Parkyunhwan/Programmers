import string
def solution(s):
    new=s.split(' ')
    a=[]
    for i in new:
        s=""
        print(i)
        for j in range(len(i)):
            if(j%2==0):
                s+=i[j].upper()
            else:
                s+=i[j].lower()
        a.append(s)
    return  ' '.join(a)
