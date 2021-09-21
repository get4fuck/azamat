line={} # строки
res={}
with open("test2.txt","r") as f:
    for i in range(10):
        line[i]=f.readline()
        stroka=line[i].split(' ')
        a=int(stroka[0])
        b=int(stroka[1])
        res[i]=(a+b)/2
with open("test1.txt","a") as result:
                    for i in range (10):
                         res[i]= str(res[i])
                         result.write(res[i]+"\n")
